import json
import zmq
import asyncio
import qtm_rt
import timeit

from assistive_arm.utils.logging import print_elapsed_time


@print_elapsed_time()
def on_packet(packet):
    """Callback function that is called everytime a data packet arrives from QTM"""
    _, markers = packet.get_3d_markers()
    force_plates = packet.get_force()[1]
    
    dict_force = {f"plate_{plate.id}": forces
                  for plate, forces in force_plates}
    # {'plate_1': [RTForce.x, RTForce.y, ...], 
    #  'plate_2': [...]}

    dict_marker = {
        f"marker_{i}": [marker.x, marker.y, marker.z]
        for i, marker in enumerate(markers)
    }
    combined_dict = {**dict_marker, **dict_force}
    marker_json = json.dumps(combined_dict)

    # Publish message to all subscribers
    publisher.send_string(marker_json)


async def setup():
    """Setup connection to QTM"""
    connection = await qtm_rt.connect("127.0.0.1")
    if connection is None:
        return

    await connection.stream_frames(components=["3d","force"], on_packet=on_packet)


if __name__ == "__main__":
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5555")
    
    asyncio.ensure_future(setup())
    asyncio.get_event_loop().run_forever()

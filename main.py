from tensorflow.python.client import device_lib
import tensorflow as tf
import os
import platform

if __name__ == "__main__":
    # Just Check OS & GPU enabled
    current_os = platform.system()

    if current_os == "Windows":
        print("Current OS : Windows")
        gpus = tf.config.experimental.list_physical_devices('GPU')

        print(gpus)
        print(device_lib.list_local_devices())
        print(tf.config.list_physical_devices('GPU'))

    elif current_os == "Darwin":
        print("Current OS : Mac")
        os.environ['TF_METAL_DEVICE'] = '/device:GPU:0'  # GPU 사용

        physical_devices = tf.config.list_physical_devices('GPU')
        if physical_devices:
            for device in physical_devices:
                print(f"Name: {device.name}, Type: {device.device_type}")
        else:
            print("GPU None")
    else:
        print("Not supported OS")

    ## Scenario Logic Start

# Drishti-
We created a detachable mobility aid that fits any standard walking cane, improving navigation for the visually impaired. It offers online functionality to detect and describe surroundings using  in real-time, while offline it uses ultrasonic sensors for path detection when Wi-Fi is unavailable, enhancing overall navigation.

This was a part of our Design Thinking course in our semister 2 at National Institute of Technology, Warangal. We were a group of 5 student who made this project possible.

1. Abstract 

Navigating dynamic environments poses significant challenges for visually impaired individuals, where traditional mobility aids may fall short in providing comprehensive situational awareness. Addressing this gap, a novel detachable mobility aid has been developed to enhance the navigational capabilities of visually impaired individuals by combining local and remote processing techniques. This innovative device seamlessly attaches to conventional mobility sticks, offering a flexible and user-friendly solution. The system employs a dual-mode approach that integrates real-time obstacle detection with advanced object recognition. A local module uses proximity sensing with the help of three ultrasonic sensors operated by an ESP-32 microcontroller to alert users about nearby obstacles through distinctive auditory cues via a piezoelectric buzzer. In parallel, the online module utilises an ESP-32 CAM to stream live visual data to a remote server, where the YOLOv8 object detection model, trained on the OpenImagesv7 dataset, analyses the scene and provides the desired spatial information. Experimental evaluations under varied environmental conditions demonstrate that the system is effective, robust, and scalable, offering significant improvements in mobility and situational awareness for visually impaired users. The integration of edge computing with cloud-based machine learning techniques not only ensures cost-effectiveness but also provides a flexible solution that can be easily adapted to various assistive technologies.

2. Backgroung of Invention

Visual impairment affects millions globally, limiting independence and mobility. Traditional aids like white canes and guide dogs offer basic assistance but fall short in complex environments. Advances in Artificial Intelligence (AI), computer vision, and sensor technology have opened new possibilities for assistive devices, enabling visually impaired individuals to navigate independently and interact with their surroundings more effectively. This invention builds upon these advancements to create a portable, AI-powered mobility aid that can transform any walking cane into a smart device, addressing limitations of existing technologies.

3. Our current features 

-> Detachable Design

Unlike existing solutions that require specialized hardware (e.g., smart sticks or wearables), this device can attach to any cane, making it cost-effective and versatile.

-> Online and ofline compatibilty 

Online - object detection and text to speech commands.

Offline - Sensor based path  detecion and pattern based buzzer alerts.

4. Future scope 

Building digital maps using machine learning model
Integrating the device with gps to give them direction to facilites nearby
SOS commands
Data logging of the device 



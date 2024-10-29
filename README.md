# gemini_ros

ROS 2 wrapper for Gemini API.

## Installation

```
$ pip install google-generativeai
```

## Topic

|Name|Type|Content|
|----|----|-------|
|/gemini/input_text|std_msgs/String|Input text(prompt) for gemini|
|/gemini/output_text|std_msgs/String|Output text(response) from gemini|

## Usage

###
```
$ export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
$ ros2 run gemini_ros gemini_ros
```

## Run example
```
$ ros2 topic pub /gemini/input_text std_msgs/msg/String "{data: 'Hi, who are you?'}" --once
```
```
$ ros2 topic echo /gemini/output_text
```

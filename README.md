# simple-turtlesim-game

A beginner-level ROS 2 micro-project demonstrating node communication and basic control loops using Turtlesim.

---

## Prerequisites

* **OS:** Ubuntu 24.04 (tested)
* **ROS 2:** Jazzy Jalisco (or newer)
* **Dependencies:**

  * `rclpy`
  * `geometry_msgs`
  * `turtlesim`

---

## ROS 2 Installation

If ROS 2 is not installed, follow the [official ROS 2 Jazzy installation guide](https://docs.ros.org/en/jazzy/Installation.html)

---

## Workspace Setup

Create a ROS 2 workspace and clone the repository:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

git clone https://github.com/Bhagabanta-Giri/simple-turtlesim-game.git
```

Build the workspace:

```bash
cd ~/ros2_ws
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

To avoid sourcing manually every time, add it to your shell configuration:

```bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## Installation & Building

Navigate to your ROS 2 workspace:

```bash
cd ~/ros2_ws
```

Build only this package:

```bash
colcon build --packages-select game_one
```

Source the workspace:

```bash
source install/setup.bash
```

---

## How to Play

Due to how ROS 2 handles raw keyboard inputs, this game requires a two-terminal setup.

The above setup steps must be done in both the terminals.

### Step 1: Start the Controls

Open your first terminal and run:

```bash
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtle_teleop_key
```

### Step 2: Launch the Game

Open the second terminal and run:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch game_one game_launch.py
```

Immediately switch to first terminal! Or the police will catch you!

### Step 3: Gameplay

Keep the teleop terminal focused and use the arrow keys to control the **Thief** turtle.

If the **Police** turtle catches you:

* The simulation stops.
* Your survival time is displayed in the first terminal.

---

## Reporting Issues

Found a bug or unexpected behavior?

Please open a GitHub Issue.

---

## Contributing

Suggestions and new features are always welcome.

If you have an idea to improve the project or expand the gameplay, feel free to submit a pull request.

### Feature Contribution Workflow

1. Fork the repository.

2. Clone your fork:

    ```bash
    git clone https://github.com/Bhagabanta-Giri/simple-turtlesim-game.git
    ```

3. Create a feature branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. Make your changes.

5. Commit your work:

    ```bash
    git commit -m "Add brief description of feature"
    ```

6. Push the branch:

    ```bash
    git push origin feature/your-feature-name
    ```

7. Open a Pull Request to the main repository.

---

## License

This project is licensed under the MIT License.

---

## Maintainer

[bhagabantagiri@gmail.com](mailto:bhagabantagiri@gmail.com)

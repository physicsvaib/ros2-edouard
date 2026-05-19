#include "rclcpp.hpp"


class RobotNewsPub: public rclcpp::Node{
    public:
        RobotNewsPub() : Node("Robot_News_Pub"){

        }

    private:
        
}

int main(int argc, char** argv){
    rclcpp::init(argc, argv);

    rclcpp::spin(node);

    rclcpp::shutdown()
}
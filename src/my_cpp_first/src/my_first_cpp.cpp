#include "rclcpp/rclcpp.hpp"

class SampleNode: public rclcpp::Node {
public:
    SampleNode(): Node("Sample_Cpp"){
        RCLCPP_INFO(this->get_logger(), "Hello Cpp that was made by me.");
        timer = this->create_wall_timer(std::chrono::seconds(1), std::bind(&SampleNode::Printer, this));
        
    }
private:
    int counter = 0;

    void Printer(){
        RCLCPP_INFO(this->get_logger(), "Printer Printing %d", counter++);
    }

    rclcpp::TimerBase::SharedPtr timer;

};

int main(int argc, char** argv){
    rclcpp::init(argc, argv);

    auto node = std::make_shared<SampleNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    
    return 0;
}
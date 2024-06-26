#include <iostream>
#include <libfreenect.hpp>
#include <opencv2/opencv.hpp>
#include <vector>

class MyFreenectDevice : public Freenect::FreenectDevice {
public:
    MyFreenectDevice(freenect_context *_ctx, int _index)
        : Freenect::FreenectDevice(_ctx, _index), m_buffer_depth(640*480) {}

    void VideoCallback(void* _rgb, uint32_t timestamp) {
        std::cout << "RGB callback" << std::endl;
    }

    void DepthCallback(void* _depth, uint32_t timestamp) {
        cv::Mat depthMat(cv::Size(640,480), CV_16UC1, _depth);
        cv::imshow("Depth", depthMat);
    }

    std::vector<uint8_t> m_buffer_depth;

private:
    std::vector<uint16_t> m_buffer_depth;  // Using uint16_t as each depth value is 11 bits, fits in 16 bits
};



int main() {
    Freenect::Freenect freenect;
    MyFreenectDevice& device = freenect.createDevice<MyFreenectDevice>(0);
    device.startVideo();
    device.startDepth();
    cv::namedWindow("Depth");
    cv::startWindowThread();

    while (cv::waitKey(10) != 27) {
        // press ESC to exit
    }

    device.stopVideo();
    device.stopDepth();
    return 0;
}

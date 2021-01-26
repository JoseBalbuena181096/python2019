#include<ros/ros.h>
#include <std_msgs/Int16.h>
#include "opencv2/opencv.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
 

using namespace std;
using namespace cv;

int main(int argc, char** argv){
  ros::init(argc, argv, "pink");
  ros::NodeHandle n;
  ros::Publisher posicion_pub = n.advertise<std_msgs::Int16>("/posicion", 1000);
  std_msgs::Int16 msg_posicion;
  // Create a VideoCapture object and open the input file
  VideoCapture cap; 
  cap.open(0); //seleccionamos nuestra webcam
    
  // Check if camera opened successfully
  if(!cap.isOpened()){
    cout << "Error opening video stream or file" << endl;
    return -1;
  }

  //namedWindow("Control",CV_WINDOW_AUTOSIZE);

  //int iLowH = 0;
  //int iHighH = 179;

  //int iLowS = 0;
  //int iHighS = 255;

  //int iLowV = 0;
  //int iHighV = 255;

  //cvCreateTrackbar("LowH", "Control", &iLowH,179);
  //cvCreateTrackbar("HighH", "Control", &iHighH,179);

  //cvCreateTrackbar("LowS", "Control", &iLowS,255);
  //cvCreateTrackbar("HighS", "Control", &iHighS,255);

  //cvCreateTrackbar("LowV", "Control", &iLowV,255);
  //cvCreateTrackbar("HighV", "Control", &iHighV,255);

  while(1)
  {
    Mat imagen,salida; //matriz de captura de la salida
    // Capture frame-by-frame
    cap >> imagen;
    // If the frame is empty, break immediately
    if (imagen.empty())
      break;
    Mat hsv;
    cvtColor(imagen, hsv, COLOR_BGR2HSV);
    Mat mascara_baja,mascara_alta;
    inRange(hsv, Scalar(94, 128, 12), Scalar(179, 255, 255), mascara_baja);
   // inRange(hsv, Scalar(170, 120, 70), Scalar(180, 255, 255), mascara_alta);
   // mascara_baja = mascara_baja + mascara_alta;
	Mat kernel = Mat::ones(3,3, CV_32F);
    morphologyEx(mascara_baja,mascara_baja,cv::MORPH_OPEN,kernel);
    morphologyEx(mascara_baja,mascara_baja,cv::MORPH_DILATE,kernel);
    bitwise_and(imagen,imagen,salida,mascara_baja);
    Moments m = moments(mascara_baja,true);
    if(m.m00>5000){
        Point p(m.m10/m.m00,m.m01/m.m00);
        circle(salida,p, 5, Scalar(255,0,0),5);
        msg_posicion.data = p.x;
        posicion_pub.publish(msg_posicion);
        ROS_INFO("(%d)", msg_posicion.data);
    }
    //imshow( "Frame", mask1);
    imshow( "NAHU FLORES", salida);
    // Press  ESC on keyboard to exit
    char c=(char)waitKey(25);
    if(c==27)
      break;
	  // Also relese all the mat created in the code to avoid memory leakage.
  	imagen.release(),hsv.release(),mascara_baja.release(),mascara_alta.release();
  }
  // When everything done, release the video capture object
  cap.release();
  // Closes all the frames
  destroyAllWindows();
  return 0;
}

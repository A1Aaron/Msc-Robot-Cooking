// Generated by gencpp from file mycobot_communication/MycobotCoords.msg
// DO NOT EDIT!


#ifndef MYCOBOT_COMMUNICATION_MESSAGE_MYCOBOTCOORDS_H
#define MYCOBOT_COMMUNICATION_MESSAGE_MYCOBOTCOORDS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mycobot_communication
{
template <class ContainerAllocator>
struct MycobotCoords_
{
  typedef MycobotCoords_<ContainerAllocator> Type;

  MycobotCoords_()
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , rx(0.0)
    , ry(0.0)
    , rz(0.0)  {
    }
  MycobotCoords_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , rx(0.0)
    , ry(0.0)
    , rz(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _rx_type;
  _rx_type rx;

   typedef float _ry_type;
  _ry_type ry;

   typedef float _rz_type;
  _rz_type rz;





  typedef boost::shared_ptr< ::mycobot_communication::MycobotCoords_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mycobot_communication::MycobotCoords_<ContainerAllocator> const> ConstPtr;

}; // struct MycobotCoords_

typedef ::mycobot_communication::MycobotCoords_<std::allocator<void> > MycobotCoords;

typedef boost::shared_ptr< ::mycobot_communication::MycobotCoords > MycobotCoordsPtr;
typedef boost::shared_ptr< ::mycobot_communication::MycobotCoords const> MycobotCoordsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mycobot_communication::MycobotCoords_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mycobot_communication::MycobotCoords_<ContainerAllocator1> & lhs, const ::mycobot_communication::MycobotCoords_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.rx == rhs.rx &&
    lhs.ry == rhs.ry &&
    lhs.rz == rhs.rz;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mycobot_communication::MycobotCoords_<ContainerAllocator1> & lhs, const ::mycobot_communication::MycobotCoords_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mycobot_communication

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mycobot_communication::MycobotCoords_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mycobot_communication::MycobotCoords_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mycobot_communication::MycobotCoords_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "740a0696f94797c91679d50dca7e75ad";
  }

  static const char* value(const ::mycobot_communication::MycobotCoords_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x740a0696f94797c9ULL;
  static const uint64_t static_value2 = 0x1679d50dca7e75adULL;
};

template<class ContainerAllocator>
struct DataType< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mycobot_communication/MycobotCoords";
  }

  static const char* value(const ::mycobot_communication::MycobotCoords_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 z\n"
"float32 rx\n"
"float32 ry\n"
"float32 rz\n"
;
  }

  static const char* value(const ::mycobot_communication::MycobotCoords_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.rx);
      stream.next(m.ry);
      stream.next(m.rz);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MycobotCoords_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mycobot_communication::MycobotCoords_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mycobot_communication::MycobotCoords_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "rx: ";
    Printer<float>::stream(s, indent + "  ", v.rx);
    s << indent << "ry: ";
    Printer<float>::stream(s, indent + "  ", v.ry);
    s << indent << "rz: ";
    Printer<float>::stream(s, indent + "  ", v.rz);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYCOBOT_COMMUNICATION_MESSAGE_MYCOBOTCOORDS_H

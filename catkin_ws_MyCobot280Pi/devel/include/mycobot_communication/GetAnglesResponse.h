// Generated by gencpp from file mycobot_communication/GetAnglesResponse.msg
// DO NOT EDIT!


#ifndef MYCOBOT_COMMUNICATION_MESSAGE_GETANGLESRESPONSE_H
#define MYCOBOT_COMMUNICATION_MESSAGE_GETANGLESRESPONSE_H


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
struct GetAnglesResponse_
{
  typedef GetAnglesResponse_<ContainerAllocator> Type;

  GetAnglesResponse_()
    : joint_1(0.0)
    , joint_2(0.0)
    , joint_3(0.0)
    , joint_4(0.0)
    , joint_5(0.0)
    , joint_6(0.0)  {
    }
  GetAnglesResponse_(const ContainerAllocator& _alloc)
    : joint_1(0.0)
    , joint_2(0.0)
    , joint_3(0.0)
    , joint_4(0.0)
    , joint_5(0.0)
    , joint_6(0.0)  {
  (void)_alloc;
    }



   typedef float _joint_1_type;
  _joint_1_type joint_1;

   typedef float _joint_2_type;
  _joint_2_type joint_2;

   typedef float _joint_3_type;
  _joint_3_type joint_3;

   typedef float _joint_4_type;
  _joint_4_type joint_4;

   typedef float _joint_5_type;
  _joint_5_type joint_5;

   typedef float _joint_6_type;
  _joint_6_type joint_6;





  typedef boost::shared_ptr< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetAnglesResponse_

typedef ::mycobot_communication::GetAnglesResponse_<std::allocator<void> > GetAnglesResponse;

typedef boost::shared_ptr< ::mycobot_communication::GetAnglesResponse > GetAnglesResponsePtr;
typedef boost::shared_ptr< ::mycobot_communication::GetAnglesResponse const> GetAnglesResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator1> & lhs, const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator2> & rhs)
{
  return lhs.joint_1 == rhs.joint_1 &&
    lhs.joint_2 == rhs.joint_2 &&
    lhs.joint_3 == rhs.joint_3 &&
    lhs.joint_4 == rhs.joint_4 &&
    lhs.joint_5 == rhs.joint_5 &&
    lhs.joint_6 == rhs.joint_6;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator1> & lhs, const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mycobot_communication

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8ce9dd71b812ac669ff127f95e5ce8ab";
  }

  static const char* value(const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8ce9dd71b812ac66ULL;
  static const uint64_t static_value2 = 0x9ff127f95e5ce8abULL;
};

template<class ContainerAllocator>
struct DataType< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mycobot_communication/GetAnglesResponse";
  }

  static const char* value(const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"float32 joint_1\n"
"float32 joint_2\n"
"float32 joint_3\n"
"float32 joint_4\n"
"float32 joint_5\n"
"float32 joint_6\n"
"\n"
;
  }

  static const char* value(const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint_1);
      stream.next(m.joint_2);
      stream.next(m.joint_3);
      stream.next(m.joint_4);
      stream.next(m.joint_5);
      stream.next(m.joint_6);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetAnglesResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mycobot_communication::GetAnglesResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mycobot_communication::GetAnglesResponse_<ContainerAllocator>& v)
  {
    s << indent << "joint_1: ";
    Printer<float>::stream(s, indent + "  ", v.joint_1);
    s << indent << "joint_2: ";
    Printer<float>::stream(s, indent + "  ", v.joint_2);
    s << indent << "joint_3: ";
    Printer<float>::stream(s, indent + "  ", v.joint_3);
    s << indent << "joint_4: ";
    Printer<float>::stream(s, indent + "  ", v.joint_4);
    s << indent << "joint_5: ";
    Printer<float>::stream(s, indent + "  ", v.joint_5);
    s << indent << "joint_6: ";
    Printer<float>::stream(s, indent + "  ", v.joint_6);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYCOBOT_COMMUNICATION_MESSAGE_GETANGLESRESPONSE_H

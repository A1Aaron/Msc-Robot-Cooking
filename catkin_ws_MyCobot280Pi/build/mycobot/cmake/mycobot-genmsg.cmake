# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mycobot: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imycobot:/home/ubuntu/catkin_ws/src/mycobot/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mycobot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_custom_target(_mycobot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mycobot" "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mycobot
  "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mycobot
)

### Generating Services

### Generating Module File
_generate_module_cpp(mycobot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mycobot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mycobot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mycobot_generate_messages mycobot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_dependencies(mycobot_generate_messages_cpp _mycobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mycobot_gencpp)
add_dependencies(mycobot_gencpp mycobot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mycobot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(mycobot
  "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mycobot
)

### Generating Services

### Generating Module File
_generate_module_eus(mycobot
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mycobot
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(mycobot_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(mycobot_generate_messages mycobot_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_dependencies(mycobot_generate_messages_eus _mycobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mycobot_geneus)
add_dependencies(mycobot_geneus mycobot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mycobot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mycobot
  "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mycobot
)

### Generating Services

### Generating Module File
_generate_module_lisp(mycobot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mycobot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mycobot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mycobot_generate_messages mycobot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_dependencies(mycobot_generate_messages_lisp _mycobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mycobot_genlisp)
add_dependencies(mycobot_genlisp mycobot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mycobot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(mycobot
  "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mycobot
)

### Generating Services

### Generating Module File
_generate_module_nodejs(mycobot
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mycobot
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(mycobot_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(mycobot_generate_messages mycobot_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_dependencies(mycobot_generate_messages_nodejs _mycobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mycobot_gennodejs)
add_dependencies(mycobot_gennodejs mycobot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mycobot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mycobot
  "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mycobot
)

### Generating Services

### Generating Module File
_generate_module_py(mycobot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mycobot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mycobot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mycobot_generate_messages mycobot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/mycobot/msg/joint.msg" NAME_WE)
add_dependencies(mycobot_generate_messages_py _mycobot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mycobot_genpy)
add_dependencies(mycobot_genpy mycobot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mycobot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mycobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mycobot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(mycobot_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mycobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mycobot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(mycobot_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mycobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mycobot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(mycobot_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mycobot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mycobot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(mycobot_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mycobot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mycobot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mycobot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(mycobot_generate_messages_py std_msgs_generate_messages_py)
endif()

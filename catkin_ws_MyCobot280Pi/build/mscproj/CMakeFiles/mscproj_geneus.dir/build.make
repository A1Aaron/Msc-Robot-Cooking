# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/ubuntu/cmake-3.19.8-Linux-aarch64/bin/cmake

# The command to remove a file.
RM = /home/ubuntu/cmake-3.19.8-Linux-aarch64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/catkin_ws/build

# Utility rule file for mscproj_geneus.

# Include the progress variables for this target.
include mscproj/CMakeFiles/mscproj_geneus.dir/progress.make

mscproj_geneus: mscproj/CMakeFiles/mscproj_geneus.dir/build.make

.PHONY : mscproj_geneus

# Rule to build all files generated by this target.
mscproj/CMakeFiles/mscproj_geneus.dir/build: mscproj_geneus

.PHONY : mscproj/CMakeFiles/mscproj_geneus.dir/build

mscproj/CMakeFiles/mscproj_geneus.dir/clean:
	cd /home/ubuntu/catkin_ws/build/mscproj && $(CMAKE_COMMAND) -P CMakeFiles/mscproj_geneus.dir/cmake_clean.cmake
.PHONY : mscproj/CMakeFiles/mscproj_geneus.dir/clean

mscproj/CMakeFiles/mscproj_geneus.dir/depend:
	cd /home/ubuntu/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/catkin_ws/src /home/ubuntu/catkin_ws/src/mscproj /home/ubuntu/catkin_ws/build /home/ubuntu/catkin_ws/build/mscproj /home/ubuntu/catkin_ws/build/mscproj/CMakeFiles/mscproj_geneus.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mscproj/CMakeFiles/mscproj_geneus.dir/depend


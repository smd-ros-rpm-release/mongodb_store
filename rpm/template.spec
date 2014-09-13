Name:           ros-hydro-mongodb-store-cpp-client
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS mongodb_store_cpp_client package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-mongodb-store-msgs
Requires:       ros-hydro-std-msgs
BuildRequires:  libmongo-client-devel
BuildRequires:  mongodb-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-mongodb-store-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-msgs

%description
The mongodb_store_cpp_client package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Sep 13 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.0.4-0
- Autogenerated by Bloom

* Wed Sep 10 2014 nah <nah@todo.todo> - 0.0.3-1
- Autogenerated by Bloom

* Thu Sep 04 2014 nah <nah@todo.todo> - 0.0.3-0
- Autogenerated by Bloom


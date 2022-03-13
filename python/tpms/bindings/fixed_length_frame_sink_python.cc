/*
 * Copyright 2022 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(fixed_length_frame_sink.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(74e51deda3cdda01c3853b6f643ced54)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <tpms/fixed_length_frame_sink.h>
// pydoc.h is automatically generated in the build directory
#include <fixed_length_frame_sink_pydoc.h>

void bind_fixed_length_frame_sink(py::module& m)
{

    using fixed_length_frame_sink    = ::gr::tpms::fixed_length_frame_sink;


    py::class_<fixed_length_frame_sink, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<fixed_length_frame_sink>>(m, "fixed_length_frame_sink", D(fixed_length_frame_sink))

        .def(py::init(&fixed_length_frame_sink::make),
           py::arg("frame_length"),
           py::arg("attributes"),
           D(fixed_length_frame_sink,make)
        )
        



        ;




}









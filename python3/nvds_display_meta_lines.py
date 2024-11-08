# An example on how to paint a line on NVDS
display_meta = pyds.nvds_acquire_display_meta_from_pool(batch_meta)
display_meta.num_lines = 1

py_nvosd_line_params = display_meta.line_params[0]
py_nvosd_line_params.x1=40
py_nvosd_line_params.x2=800
py_nvosd_line_params.y1=40
py_nvosd_line_params.y2=800
py_nvosd_line_params.line_width=20
py_nvosd_line_params.line_color.set(1.0,1.0,0.0,1.0)

pyds.nvds_add_display_meta_to_frame(frame_meta, display_meta)

# Velvet Shortcuts version date: 20190909
# To be used with Blender versions 2.80
# Check documentation at http://blendervelvets.org
# Author: szaszak

keyconfig_data = \
[("Screen",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
    ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.region_quadview", {"type": 'Q', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("screen.repeat_last", {"type": 'R', "value": 'PRESS', "shift": True}, None),
    ("file.execute", {"type": 'RET', "value": 'PRESS'}, None),
    ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
    ("file.cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True}, None),
    ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("render.render",
     {"type": 'F12', "value": 'PRESS'},
     {"properties":
      [("use_viewport", True),
       ],
      },
     ),
    ("render.render",
     {"type": 'F12', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("animation", True),
       ("use_viewport", True),
       ],
      },
     ),
    ("render.view_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("render.view_show", {"type": 'F11', "value": 'PRESS'}, None),
    ("render.play_rendered_anim", {"type": 'F11', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area",
     {"type": 'SPACE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("use_hide_panels", True),
       ],
      },
     ),
    ("screen.redo_last", {"type": 'F9', "value": 'PRESS'}, None),
    ("screen.scene_toggle", {"type": 'TAB', "value": 'PRESS', "shift": True}, None),
    ],
   },
  ),
 ("Animation",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("wm.context_toggle",
     {"type": 'T', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_seconds'),
       ],
      },
     ),
    ("anim.previewrange_set", {"type": 'P', "value": 'PRESS'}, None),
    ("anim.previewrange_clear", {"type": 'P', "value": 'PRESS', "alt": True}, None),
    ("anim.start_frame_set", {"type": 'HOME', "value": 'PRESS', "ctrl": True}, None),
    ("anim.start_frame_one_set", {"type": 'HOME', "value": 'PRESS', "alt": True}, None),
    ("anim.end_frame_set", {"type": 'END', "value": 'PRESS', "ctrl": True}, None),
    ("anim.end_frame_last_set", {"type": 'END', "value": 'PRESS', "alt": True}, None),
    ("anim.change_frame", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ],
   },
  ),
 ("Graph Editor",
  {"space_type": 'GRAPH_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("wm.context_toggle",
     {"type": 'H', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_handles'),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ("deselect_all", True),
       ("column", False),
       ("curves", False),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("extend", False),
       ("column", True),
       ("curves", False),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ("column", False),
       ("curves", False),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("extend", True),
       ("column", True),
       ("curves", False),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("extend", False),
       ("column", False),
       ("curves", True),
       ],
      },
     ),
    ("graph.clickselect",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("extend", True),
       ("column", False),
       ("curves", True),
       ],
      },
     ),
    ("graph.select_leftright",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("mode", 'CHECK'),
       ("extend", False),
       ],
      },
     ),
    ("graph.select_leftright",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'CHECK'),
       ("extend", True),
       ],
      },
     ),
    ("graph.select_leftright",
     {"type": 'LEFT_BRACKET', "value": 'PRESS'},
     {"properties":
      [("mode", 'LEFT'),
       ("extend", False),
       ],
      },
     ),
    ("graph.select_leftright",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS'},
     {"properties":
      [("mode", 'RIGHT'),
       ("extend", False),
       ],
      },
     ),
    ("graph.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("graph.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("graph.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("graph.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'B', "value": 'PRESS'},
     {"properties":
      [("axis_range", False),
       ("include_handles", False),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'B', "value": 'PRESS', "alt": True},
     {"properties":
      [("axis_range", True),
       ("include_handles", False),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'B', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("axis_range", False),
       ("include_handles", True),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("axis_range", True),
       ("include_handles", True),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY'},
     {"properties":
      [("tweak", True),
       ("mode", 'SET'),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},
     {"properties":
      [("tweak", True),
       ("mode", 'ADD'),
       ],
      },
     ),
    ("graph.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},
     {"properties":
      [("tweak", True),
       ("mode", 'SUB'),
       ],
      },
     ),
    ("graph.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("graph.select_lasso",
     {"type": 'EVT_TWEAK_R', "value": 'ANY', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("graph.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("graph.select_column",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("mode", 'KEYS'),
       ],
      },
     ),
    ("graph.select_column",
     {"type": 'K', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("mode", 'CFRA'),
       ],
      },
     ),
    ("graph.select_column",
     {"type": 'K', "value": 'PRESS', "shift": True},
     {"properties":
      [("mode", 'MARKERS_COLUMN'),
       ],
      },
     ),
    ("graph.select_column",
     {"type": 'K', "value": 'PRESS', "alt": True},
     {"properties":
      [("mode", 'MARKERS_BETWEEN'),
       ],
      },
     ),
    ("graph.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("graph.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("graph.select_linked", {"type": 'L', "value": 'PRESS'}, None),
    ("graph.frame_jump", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'GRAPH_MT_snap_pie'),
       ],
      },
     ),
    ("graph.mirror", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("graph.handle_type", {"type": 'V', "value": 'PRESS'}, None),
    ("graph.interpolation_type", {"type": 'T', "value": 'PRESS'}, None),
    ("graph.easing_type", {"type": 'E', "value": 'PRESS', "ctrl": True}, None),
    ("graph.smooth", {"type": 'O', "value": 'PRESS', "alt": True}, None),
    ("graph.sample", {"type": 'O', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("graph.bake", {"type": 'C', "value": 'PRESS', "alt": True}, None),
    ("wm.call_menu",
     {"type": 'X', "value": 'PRESS'},
     {"properties":
      [("name", 'GRAPH_MT_delete'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'DEL', "value": 'PRESS'},
     {"properties":
      [("name", 'GRAPH_MT_delete'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'GRAPH_MT_context_menu'),
       ],
      },
     ),
    ("graph.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("graph.keyframe_insert", {"type": 'I', "value": 'PRESS'}, None),
    ("graph.click_insert",
     {"type": 'RIGHTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("extend", False),
       ],
      },
     ),
    ("graph.click_insert",
     {"type": 'RIGHTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ],
      },
     ),
    ("graph.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("graph.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("graph.paste",
     {"type": 'V', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("flipped", True),
       ],
      },
     ),
    ("graph.previewrange_set", {"type": 'P', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("graph.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("graph.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("graph.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("graph.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("graph.fmodifier_add",
     {"type": 'M', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("only_active", False),
       ],
      },
     ),
    ("anim.channels_editable_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
    ("transform.translate", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.translate", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
    ("transform.transform",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("mode", 'TIME_EXTEND'),
       ],
      },
     ),
    ("transform.rotate", {"type": 'R', "value": 'PRESS'}, None),
    ("transform.resize", {"type": 'S', "value": 'PRESS'}, None),
    ("wm.context_toggle",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'tool_settings.use_proportional_fcurve'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'O', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_proportional_editing_falloff_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'GRAPH_MT_pivot_pie'),
       ],
      },
     ),
    ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
    ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("graph.cursor_set", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ],
   },
  ),
 ("Sequencer",
  {"space_type": 'SEQUENCE_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("sequencer.select_all",
     {"type": 'A', "value": 'PRESS'},
     {"properties":
      [("action", 'SELECT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'PRESS', "alt": True},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'I', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("action", 'INVERT'),
       ],
      },
     ),
    ("sequencer.select_all",
     {"type": 'A', "value": 'DOUBLE_CLICK'},
     {"properties":
      [("action", 'DESELECT'),
       ],
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS'},
     {"properties":
      [("type", 'SOFT'),
       ],
      },
     ),
    ("sequencer.cut",
     {"type": 'K', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'HARD'),
       ],
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS'},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.mute",
     {"type": 'H', "value": 'PRESS', "shift": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "alt": True},
     {"properties":
      [("unselected", False),
       ],
      },
     ),
    ("sequencer.unmute",
     {"type": 'H', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("unselected", True),
       ],
      },
     ),
    ("sequencer.strips_display_waveform", {"type": 'W', "value": 'PRESS'}, None),
    ("sequencer.strips_hide_waveform", {"type": 'W', "value": 'PRESS', "alt": True}, None),
    ("sequencer.lock", {"type": 'L', "value": 'PRESS', "shift": True}, None),
    ("sequencer.unlock", {"type": 'L', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("sequencer.reassign_inputs", {"type": 'R', "value": 'PRESS'}, None),
    ("sequencer.reload", {"type": 'R', "value": 'PRESS', "alt": True}, None),
    ("sequencer.reload",
     {"type": 'R', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("adjust_length", True),
       ],
      },
     ),
    ("sequencer.refresh_all", {"type": 'R', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.offset_clear", {"type": 'O', "value": 'PRESS', "alt": True}, None),
    ("sequencer.duplicate_move", {"type": 'D', "value": 'PRESS', "shift": True}, None),
    ("sequencer.fade_in_strip_start", {"type": 'F', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.fade_out_strip_end", {"type": 'F', "value": 'PRESS', "alt": True}, None),
    ("sequencer.strip_up", {"type": 'UP_ARROW', "value": 'PRESS', "alt": True}, None),
    ("sequencer.strip_down", {"type": 'DOWN_ARROW', "value": 'PRESS', "alt": True}, None),
    ("sequencer.delete", {"type": 'X', "value": 'PRESS'}, None),
    ("sequencer.delete_direct", {"type": 'DEL', "value": 'PRESS'}, None),
    ("sequencer.delete_direct_gaps", {"type": 'DEL', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.copy", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.paste", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.images_separate", {"type": 'Y', "value": 'PRESS'}, None),
    ("sequencer.meta_toggle", {"type": 'TAB', "value": 'PRESS'}, None),
    ("sequencer.meta_make", {"type": 'G', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.meta_separate", {"type": 'G', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("sequencer.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("sequencer.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("sequencer.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("sequencer.view_frame", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS'},
     {"properties":
      [("next", True),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS'},
     {"properties":
      [("next", False),
       ("center", False),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_UP', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", True),
       ("center", True),
       ],
      },
     ),
    ("sequencer.strip_jump",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "alt": True},
     {"properties":
      [("next", False),
       ("center", True),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'LEFT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'LEFT'),
       ],
      },
     ),
    ("sequencer.swap",
     {"type": 'RIGHT_ARROW', "value": 'PRESS', "alt": True},
     {"properties":
      [("side", 'RIGHT'),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS'},
     {"properties":
      [("all", False),
       ],
      },
     ),
    ("sequencer.gap_remove",
     {"type": 'BACK_SPACE', "value": 'PRESS', "shift": True},
     {"properties":
      [("all", True),
       ],
      },
     ),
    ("sequencer.gap_insert", {"type": 'EQUAL', "value": 'PRESS', "shift": True}, None),
    ("sequencer.strips_concatenate_selected", {"type": 'C', "value": 'PRESS', "shift": True}, None),
    ("sequencer.snap", {"type": 'S', "value": 'PRESS', "shift": True}, None),
    ("sequencer.snap_selected_to_playhead", {"type": 'C', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("sequencer.snap_selected_to_timelinestart", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("sequencer.slight_desync_adjust", {"type": 'D', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("sequencer.swap_inputs", {"type": 'S', "value": 'PRESS', "alt": True}, None),
    ("sequencer.strips_deinterlace", {"type": 'I', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("sequencer.strips_deinterlace_off", {"type": 'I', "value": 'PRESS', "shift": True, "alt": True}, None),
    ("sequencer.cut_multicam",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("camera", 1),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("camera", 2),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("camera", 3),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FOUR', "value": 'PRESS'},
     {"properties":
      [("camera", 4),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'FIVE', "value": 'PRESS'},
     {"properties":
      [("camera", 5),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SIX', "value": 'PRESS'},
     {"properties":
      [("camera", 6),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'SEVEN', "value": 'PRESS'},
     {"properties":
      [("camera", 7),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'EIGHT', "value": 'PRESS'},
     {"properties":
      [("camera", 8),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'NINE', "value": 'PRESS'},
     {"properties":
      [("camera", 9),
       ],
      },
     ),
    ("sequencer.cut_multicam",
     {"type": 'ZERO', "value": 'PRESS'},
     {"properties":
      [("camera", 10),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ("deselect_all", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("extend", False),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("extend", True),
       ("linked_handle", True),
       ("left_right", 'NONE'),
       ("linked_time", False),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("extend", False),
       ("linked_handle", False),
       ("left_right", 'MOUSE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("extend", True),
       ("linked_handle", False),
       ("left_right", 'MOUSE'),
       ("linked_time", True),
       ],
      },
     ),
    ("sequencer.select_more", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_less", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS'},
     {"properties":
      [("extend", False),
       ],
      },
     ),
    ("sequencer.select_linked_pick",
     {"type": 'L', "value": 'PRESS', "shift": True},
     {"properties":
      [("extend", True),
       ],
      },
     ),
    ("sequencer.select_linked", {"type": 'L', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY'},
     {"properties":
      [("mode", 'SET'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "shift": True},
     {"properties":
      [("mode", 'ADD'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box",
     {"type": 'EVT_TWEAK_L', "value": 'ANY', "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ("tweak", True),
       ],
      },
     ),
    ("sequencer.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("sequencer.select_grouped", {"type": 'G', "value": 'PRESS', "shift": True}, None),
    ("wm.call_menu",
     {"type": 'A', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'SEQUENCER_MT_add'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'C', "value": 'PRESS'},
     {"properties":
      [("name", 'SEQUENCER_MT_change'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'SEQUENCER_MT_context_menu'),
       ],
      },
     ),
    ("sequencer.slip", {"type": 'S', "value": 'PRESS'}, None),
    ("wm.context_set_int",
     {"type": 'O', "value": 'PRESS'},
     {"properties":
      [("data_path", 'scene.sequence_editor.overlay_frame'),
       ("value", 0),
       ],
      },
     ),
    ("transform.seq_slide", {"type": 'G', "value": 'PRESS'}, None),
    ("transform.seq_slide", {"type": 'EVT_TWEAK_L', "value": 'ANY'}, None),
    ("transform.transform",
     {"type": 'E', "value": 'PRESS'},
     {"properties":
      [("mode", 'TIME_EXTEND'),
       ],
      },
     ),
    ("marker.add", {"type": 'M', "value": 'PRESS'}, None),
    ("marker.rename", {"type": 'M', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.marker_delete_closest", {"type": 'M', "value": 'PRESS', "alt": True}, None),
    ("sequencer.marker_goto_left", {"type": 'LEFT_ARROW', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.marker_goto_right", {"type": 'RIGHT_ARROW', "value": 'PRESS', "ctrl": True}, None),
    ("sequencer.timeline_loop_selected", {"type": 'L', "value": 'PRESS', "shift": True, "ctrl": True, "alt": True}, None),
    ("sequencer.timeline_preview_select", {"type": 'A', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("sequencer.view_selected_context", {"type": 'END', "value": 'PRESS'}, None),
    ("sequencer.timeline_zoom_in_10s", {"type": 'HOME', "value": 'PRESS', "shift": True}, None),
    ("sequencer.timeline_zoom_out_10s", {"type": 'END', "value": 'PRESS', "shift": True}, None),
    ("sequencer.timeline_zoom_out_10s", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("sequencer.timeline_zoom_out_xy", {"type": 'END', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("sequencer.timeline_zoom_to_playhead", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(os.path.splitext(os.path.basename(__file__))[0], keyconfig_data)

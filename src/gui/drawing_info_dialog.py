#
#  (C) Copyright 2017  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import tkinter

from importers.dxf_entity_type import *


class DrawingInfoDialog(tkinter.Toplevel):
    def __init__(self, parent, drawing_statistic):
        tkinter.Toplevel.__init__(self, parent)

        # don't display the dialog in list of opened windows
        self.transient(parent)
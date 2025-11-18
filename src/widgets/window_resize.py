from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QCursor

def toggle_maximize(window: QMainWindow):
    if window.isMaximized():
        window.showNormal()
        if hasattr(window, 'resize_handler'):
            window.resize_handler.moving = False
            window.resize_handler.toggle_maximize_status = True
    else:
        window.showMaximized()
        if hasattr(window, 'resize_handler'):
            window.resize_handler.moving = True
            window.resize_handler.toggle_maximize_status = True


class ResizeHandler:
    def __init__(self, window, margin=5):
        self.window = window
        self.margin = margin
        self.dragging = False
        self.moving = False
        self.drag_direction = None
        self.drag_start_pos = None
        self.drag_start_geometry = None
        self.toggle_maximize_status = False

        self.window.setMouseTracking(True)
    
    def get_resize_direction(self, pos):
        x, y = pos.x(), pos.y()
        w, h = self.window.width(), self.window.height()
        # print(f"x={x}, y={y}, w={w}, h={h}, margin={self.margin}")
        # print(f"x<=margin: {x<=self.margin}, x>=w-margin: {x>=w-self.margin}")
        # print(f"y<=margin: {y<=self.margin}, y>=h-margin: {y>=h-self.margin}")
            
        if x <= self.margin and y <= self.margin:
            return 'top_left'
        elif x >= w - self.margin and y <= self.margin:
            return 'top_right'
        elif x <= self.margin and y >= h - self.margin:
            return 'bottom_left'
        elif x >= w - self.margin and y >= h - self.margin:
            return 'bottom_right'
        elif x <= self.margin:
            return 'left'
        elif x >= w - self.margin:
            return 'right'
        elif y <= self.margin:
            return 'top'
        elif y >= h - self.margin:
            return 'bottom'
        return None
    
    def direction_to_cursor(self, direction):
        cursors = {
            'top_left': Qt.CursorShape.SizeFDiagCursor,
            'top_right': Qt.CursorShape.SizeBDiagCursor, 
            'bottom_left': Qt.CursorShape.SizeBDiagCursor,
            'bottom_right': Qt.CursorShape.SizeFDiagCursor,
            'left': Qt.CursorShape.SizeHorCursor,
            'right': Qt.CursorShape.SizeHorCursor,
            'top': Qt.CursorShape.SizeVerCursor,
            'bottom': Qt.CursorShape.SizeVerCursor
        }
        return cursors.get(direction, Qt.CursorShape.ArrowCursor)

    def mouse_press(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_direction = self.get_resize_direction(event.pos())
            if self.drag_direction:
                self.dragging = True
                self.drag_start_pos = event.globalPos()
                self.drag_start_geometry = self.window.geometry()
                return True
            else:
                self.moving = True
        return False

    def mouse_move(self, event):
        if self.moving:
            return False

        # print("MOUSE MOVE CALLED - EVENT RECEIVED")
        # print(f"Dragging: {self.dragging}")
        
        if not self.dragging:
            direction = self.get_resize_direction(event.pos())
            # print(f"Direction: {direction}")
            
            if direction:
                # print("Has direction - returning True")
                cursor_type = self.direction_to_cursor(direction)
                self.window.setCursor(QCursor(cursor_type))
                return True
            else:
                # print("No direction - returning False")
                self.window.unsetCursor()
                return False
        else:
            # print("Dragging - returning True")
            self.handle_resize(event.globalPos())
            return True

    def mouse_release(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.dragging:
            self.dragging = False
            self.drag_direction = None
            self.window.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            return True
        elif self.moving:
            self.moving = False
            return True
        return False

    def handle_resize(self, global_pos):
        if not self.dragging or not self.drag_direction:
            return
            
        delta = global_pos - self.drag_start_pos
        new_geometry = QRect(self.drag_start_geometry)
        
        direction = self.drag_direction
        
        if 'left' in direction:
            new_geometry.setLeft(new_geometry.left() + delta.x())
        if 'right' in direction:
            new_geometry.setRight(new_geometry.right() + delta.x())
        if 'top' in direction:
            new_geometry.setTop(new_geometry.top() + delta.y())
        if 'bottom' in direction:
            new_geometry.setBottom(new_geometry.bottom() + delta.y())
        
        if new_geometry.width() >= self.window.minimumWidth() and new_geometry.height() >= self.window.minimumHeight():
            self.window.setGeometry(new_geometry)
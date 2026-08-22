STYLE = """
QMainWindow, QWidget { background: #07111f; color: #e8f0ff; font-size: 13px; }
QLabel#brandTitle { font-size: 22px; font-weight: 700; color: #f2f7ff; }
QLabel#brandSubtitle { color: #8aa4c7; }
QLabel#statusLabel { color: #8fa7c5; padding: 3px 0; }
QLabel#previewTitle { font-size: 17px; font-weight: 700; color: #58d7ff; }
QLineEdit, QPlainTextEdit, QTableWidget, QTreeView, QComboBox {
  background: #0d1b2d; border: 1px solid #1e3550; border-radius: 7px; padding: 7px; color: #eaf2ff;
}
QLineEdit:focus, QPlainTextEdit:focus, QComboBox:focus, QTreeView:focus { border: 1px solid #38cfff; }
QPushButton { background: #14698d; border: 0; border-radius: 7px; padding: 8px 14px; color: white; font-weight: 600; }
QPushButton:hover { background: #1880aa; }
QPushButton:pressed { background: #115b7b; }
QPushButton:disabled { background: #253449; color: #728199; }
QPushButton#secondaryButton { background: #17263b; border: 1px solid #2d4664; }
QPushButton#secondaryButton:hover { background: #203652; }
QPushButton#dangerButton { background: #612a36; border: 1px solid #8d3f50; }
QPushButton#dangerButton:hover { background: #7b3343; }
QTabWidget::pane { border: 1px solid #1e3550; border-radius: 7px; top: -1px; }
QTabBar::tab { background: #0b1829; padding: 10px 19px; margin-right: 2px; color: #94a9c5; }
QTabBar::tab:selected { background: #133457; color: #ffffff; border-bottom: 2px solid #4fd9ff; }
QHeaderView::section { background: #11233a; color: #cbdaf0; padding: 8px; border: 0; }
QTableWidget, QTreeView { gridline-color: #172941; selection-background-color: #153d61; }
QSplitter::handle { background: #12243a; height: 4px; }
QCheckBox { spacing: 7px; }
"""

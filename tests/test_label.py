#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test class MLabel.
"""
import pytest

from dayu_widgets.label import MLabel
from dayu_widgets.qt import Qt, QWidget, QVBoxLayout


@pytest.mark.parametrize('cls,text,attr', (
    (MLabel.h1, 'any', 1),
    (MLabel.h2, '', 2),
    (MLabel.h3, 'test', 3),
    (MLabel.h4, 'doesn\'t matter', 4)
))
def test_label_dayu_level(qtbot, cls, text, attr):
    """Test MLabel with different level"""
    label = cls(text)
    qtbot.addWidget(label)

    assert label.get_dayu_level() == attr
    assert label.text() == text


@pytest.mark.parametrize('cls,text,attr', (
    (MLabel, 'any', ''),
    (MLabel.secondary, 'Secondary', 'secondary'),
    (MLabel.warning, 'Warning', 'warning'),
    (MLabel.danger, 'Danger', 'danger')
))
def test_label_dayu_type(qtbot, cls, text, attr):
    """Test MLabel with different type"""
    label = cls(text)
    qtbot.addWidget(label)

    assert label.get_dayu_type() == attr
    assert label.text() == text


@pytest.mark.parametrize('text, cls, attr', (
    ('Mark', MLabel.mark, 'dayu_mark'),
    ('Code', MLabel.code, 'dayu_code'),
    ('Underline', MLabel.underline, 'dayu_underline'),
    ('Delete', MLabel.delete, 'dayu_delete'),
    ('Strong', MLabel.strong, 'dayu_strong')
))
def test_label_dayu_style(qtbot, cls, text, attr):
    """Test MLabel with different style"""
    label = cls(text)
    qtbot.addWidget(label)

    assert label.property(attr)
    assert label.text() == text


@pytest.mark.parametrize('text, elide', (
    ('test' * 30, True),
    ('test', False)
))
def test_label_elide_mode(qtbot, text, elide):
    """Test MLabel elide mode"""
    main_widget = QWidget()
    main_widget.setGeometry(0, 0, 30, 200)
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)

    label_left = MLabel()
    label_left.set_elide_mode(Qt.ElideLeft)
    label_left.setText(text)
    label_right = MLabel()
    label_right.set_elide_mode(Qt.ElideRight)
    label_right.setText(text)
    label_center = MLabel(text)
    label_center.set_elide_mode(Qt.ElideMiddle)
    label_center.setText(text)

    main_lay.addWidget(label_left)
    main_lay.addWidget(label_right)
    main_lay.addWidget(label_center)

    qtbot.addWidget(main_widget)

    main_widget.show()
    ellipsis = u'…'
    if elide:
        assert label_left.property('text').startswith(ellipsis)
        assert label_right.property('text').endswith(ellipsis)
        center_text = label_center.property('text')
        assert center_text.count(ellipsis) \
               and not center_text.endswith(ellipsis)
    else:
        assert label_left.property('text') == label_left.text()
        assert label_right.property('text') == label_right.text()
        assert label_center.property('text') == label_center.text()

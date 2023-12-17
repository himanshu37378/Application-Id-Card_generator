MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDToolbar:
            title: "Dice Roller"
    Image:
        size_hint_y: 0.4
        size_hint_x: 0.4
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        source: "logo-gne.png"

    MDRaisedButton:
        text: "ROLL"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
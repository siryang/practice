import pygtk
pygtk.require("2.0")

import gtk

class MainFream:
    def __init__(self):
        self.m_closeTime = 0

        self.m_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.m_window.set_border_width(300)

        self.m_window.connect("delete_event", self.delete_event)
        self.m_window.connect("destroy", self.destroy)

        self.m_buttonClose = gtk.Button("Close")
        #self.m_buttonClose.connect("clicked", self.destroy)
        self.m_buttonClose.connect_object("clicked", gtk.Widget.destroy, self.m_window)

        self.m_window.add(self.m_buttonClose)

        self.m_buttonClose.show()
        self.m_window.show()

    # click "X" then call "delete_event-->destory
    def delete_event(self, widget, data=None):
        print("delete event happened")
        if self.m_closeTime == 0:
            print("First time to close")
            self.m_closeTime = 1
            return True
        else:
            print("Second time to close")
            return False


    def destroy(self, widget, data=None):
        print("destroy")
        gtk.main_quit()

    def main(self):
        gtk.main()


def main():
    print(__file__)

    mainFream = MainFream()
    mainFream.main()


if __name__ == "__main__":
    main()



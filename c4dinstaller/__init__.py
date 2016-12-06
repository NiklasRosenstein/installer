# C4D Installer
# Copyright (C) 2016  Niklas Rosenstein
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from . import ui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class AboutPage(ui.form('page00about')):
  pass


class WelcomePage(ui.form('page01welcome')):
  pass


class EulaPage(ui.form('page02eula')):
  pass


class FeaturesPage(ui.form('page03features')):
  pass


class TargetPage(ui.form('page04target')):
  pass


class InstallPage(ui.form('page05install')):
  pass


class EndPage(ui.form('page06end')):
  pass


class Installer(ui.form('installer')):

  def initForm(self):
    self.aboutPage = AboutPage()
    self.welcomePage = WelcomePage()
    self.eulaPage = EulaPage()
    self.featuresPage = FeaturesPage()
    self.targetPage = TargetPage()
    self.installPage = InstallPage()
    self.endPage = EndPage()

    self.stackedPages.addWidget(self.aboutPage)
    self.stackedPages.addWidget(self.welcomePage)
    self.stackedPages.addWidget(self.eulaPage)
    self.stackedPages.addWidget(self.featuresPage)
    self.stackedPages.addWidget(self.targetPage)
    self.stackedPages.addWidget(self.installPage)
    self.stackedPages.addWidget(self.endPage)

    self.setCurrentPage(self.welcomePage)
    self.aboutButton.clicked.connect(self.aboutButton_clicked)

  def setCurrentPage(self, page=None, save=True):
    if page is None:
      page = self.currentPage
    if save:
      self.currentPage = page
    self.stackedPages.setCurrentWidget(page)

  def aboutButton_clicked(self):
    if self.stackedPages.currentWidget() == self.aboutPage:
      self.aboutButton.setText("About")
      self.setCurrentPage()
    else:
      self.aboutButton.setText("Back")
      self.setCurrentPage(self.aboutPage, False)


def main():
  app = QApplication(sys.argv)
  wnd = Installer()
  wnd.show()
  return app.exec_()

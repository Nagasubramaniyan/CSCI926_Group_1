def TC_27_30():
    #Closes the 'wnd_' window.
    Aliases.ApplicationFrameHost.wnd_.Close()
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.imageLogoPngVA2a176ee3cee251ffdd object equals 118.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.imageLogoPngVA2a176ee3cee251ffdd, "ScreenLeft", cmpEqual, 118)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonQuit object equals 1135.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonQuit, "ScreenLeft", cmpEqual, 1135)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonLogout object equals 1189.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonLogout, "ScreenLeft", cmpEqual, 1189)

def TC_31_55():
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbar object equals 113.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbar, "ScreenLeft", cmpEqual, 113)
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8891/notebooks/Untitled.ipynb")
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.panel object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panel, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile object equals 114.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile, "ScreenLeft", cmpEqual, 114)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.linkEdit object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.linkEdit, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.linkEdit object equals 165.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.linkEdit, "ScreenLeft", cmpEqual, 165)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.linkView object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.linkView, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.linkView object equals 217.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.linkView, "ScreenLeft", cmpEqual, 217)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode5.linkInsert object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode5.linkInsert, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode5.linkInsert object equals 275.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode5.linkInsert, "ScreenLeft", cmpEqual, 275)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode6.linkCell object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode6.linkCell, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode6.linkCell object equals 338.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode6.linkCell, "ScreenLeft", cmpEqual, 338)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.linkKernel object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.linkKernel, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.linkKernel object equals 390.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.linkKernel, "ScreenLeft", cmpEqual, 390)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.linkWidgets object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.linkWidgets, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.linkWidgets object equals 458.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.linkWidgets, "ScreenLeft", cmpEqual, 458)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.linkHelp object equals 116.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.linkHelp, "ScreenTop", cmpEqual, 116)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.linkHelp object equals 535.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.linkHelp, "ScreenLeft", cmpEqual, 535)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.panelNotificationTrusted object equals 120.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panelNotificationTrusted, "ScreenTop", cmpEqual, 120)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.panelNotificationTrusted object equals 1098.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panelNotificationTrusted, "ScreenLeft", cmpEqual, 1098)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnodePython3 object equals 123.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnodePython3, "ScreenTop", cmpEqual, 123)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnodePython32 object equals 1170.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnodePython32, "ScreenLeft", cmpEqual, 1170)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbarContainer object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbarContainer, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbarContainer object equals 108.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panelMaintoolbarContainer, "ScreenLeft", cmpEqual, 108)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button object equals 113.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button, "ScreenLeft", cmpEqual, 113)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button2 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button2, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button2 object equals 147.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button2, "ScreenLeft", cmpEqual, 147)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button3 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button3, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button3 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button3, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button4 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button4, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button4 object equals 210.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button4, "ScreenLeft", cmpEqual, 210)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button5 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button5, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button5 object equals 240.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button5, "ScreenLeft", cmpEqual, 240)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button6 object equals 276.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button6, "ScreenLeft", cmpEqual, 276)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button7 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button7, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button7 object equals 305.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button7, "ScreenLeft", cmpEqual, 305)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button8 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button8, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button8 object equals 341.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button8, "ScreenLeft", cmpEqual, 341)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button9 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button9, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button9 object equals 400.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button9, "ScreenLeft", cmpEqual, 400)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button10 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button10, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button10 object equals 428.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button10, "ScreenLeft", cmpEqual, 428)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button11 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button11, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button11 object equals 456.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button11, "ScreenLeft", cmpEqual, 456)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.selectCellType object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.selectCellType, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.selectCellType object equals 490.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.selectCellType, "ScreenLeft", cmpEqual, 490)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.button12 object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button12, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.button12 object equals 609.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.button12, "ScreenLeft", cmpEqual, 609)

def TC_56():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8891/notebooks/Untitled.ipynb")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkFile' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkNewNotebookdropdown object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkNewNotebookdropdown, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkNewNotebookdropdown object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkNewNotebookdropdown, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeOpen.linkOpen object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeOpen.linkOpen, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeOpen.linkOpen object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeOpen.linkOpen, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeMakeACopy.linkMakeACopy object equals 217.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeMakeACopy.linkMakeACopy, "ScreenTop", cmpEqual, 217)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeMakeACopy.linkMakeACopy object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeMakeACopy.linkMakeACopy, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAs.linkSaveAs object equals 241.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAs.linkSaveAs, "ScreenTop", cmpEqual, 241)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAs.linkSaveAs object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAs.linkSaveAs, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeRename.linkRename object equals 265.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeRename.linkRename, "ScreenTop", cmpEqual, 265)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeRename.linkRename object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeRename.linkRename, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAndCheckpointCtrlS.linkSaveAndCheckpointctrlS object equals 289.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAndCheckpointCtrlS.linkSaveAndCheckpointctrlS, "ScreenTop", cmpEqual, 289)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAndCheckpointCtrlS.linkSaveAndCheckpointctrlS object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeSaveAndCheckpointCtrlS.linkSaveAndCheckpointctrlS, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown object equals 330.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown, "ScreenTop", cmpEqual, 330)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodePrintPreview.linkPrintPreview object equals 371.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodePrintPreview.linkPrintPreview, "ScreenTop", cmpEqual, 371)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodePrintPreview.linkPrintPreview object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodePrintPreview.linkPrintPreview, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkDownloadAsdropdown object equals 395.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkDownloadAsdropdown, "ScreenTop", cmpEqual, 395)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkDownloadAsdropdown object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeFile.linkDownloadAsdropdown, "ScreenLeft", cmpEqual, 115)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt object equals 477.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt, "ScreenTop", cmpEqual, 477)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt object equals 115.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt, "ScreenLeft", cmpEqual, 115)

def TC_57_66():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8891/notebooks/Untitled.ipynb")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkEdit' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.linkEdit.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellsX.linkCutCellsx object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellsX.linkCutCellsx, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellsX.linkCutCellsx object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellsX.linkCutCellsx, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellsC.linkCopyCellsc object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellsC.linkCopyCellsc, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellsC.linkCopyCellsc object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellsC.linkCopyCellsc, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeDeleteCellsDD.linkDeleteCellsdD object equals 272.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeDeleteCellsDD.linkDeleteCellsdD, "ScreenTop", cmpEqual, 272)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeDeleteCellsDD.linkDeleteCellsdD object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeDeleteCellsDD.linkDeleteCellsdD, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeSplitCellCtrlShiftMinus.linkSplitCellctrlShiftMinus object equals 337.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeSplitCellCtrlShiftMinus.linkSplitCellctrlShiftMinus, "ScreenTop", cmpEqual, 337)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeSplitCellCtrlShiftMinus.linkSplitCellctrlShiftMinus object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeSplitCellCtrlShiftMinus.linkSplitCellctrlShiftMinus, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellAbove.linkMergeCellAbove object equals 361.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellAbove.linkMergeCellAbove, "ScreenTop", cmpEqual, 361)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellAbove.linkMergeCellAbove object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellAbove.linkMergeCellAbove, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellBelow.linkMergeCellBelow object equals 385.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellBelow.linkMergeCellBelow, "ScreenTop", cmpEqual, 385)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellBelow.linkMergeCellBelow object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMergeCellBelow.linkMergeCellBelow, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellUp.linkMoveCellUp object equals 426.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellUp.linkMoveCellUp, "ScreenTop", cmpEqual, 426)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellUp.linkMoveCellUp object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellUp.linkMoveCellUp, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellDown.linkMoveCellDown object equals 450.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellDown.linkMoveCellDown, "ScreenTop", cmpEqual, 450)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellDown.linkMoveCellDown object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeMoveCellDown.linkMoveCellDown, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeEditNotebookMetadata.linkEditNotebookMetadata object equals 491.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeEditNotebookMetadata.linkEditNotebookMetadata, "ScreenTop", cmpEqual, 491)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeEditNotebookMetadata.linkEditNotebookMetadata object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeEditNotebookMetadata.linkEditNotebookMetadata, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace object equals 532.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace, "ScreenTop", cmpEqual, 532)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace object equals 532.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace, "ScreenTop", cmpEqual, 532)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeFindAndReplace.linkFindAndReplace, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellAttachments.linkCutCellAttachments object equals 573.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellAttachments.linkCutCellAttachments, "ScreenTop", cmpEqual, 573)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellAttachments.linkCutCellAttachments object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCutCellAttachments.linkCutCellAttachments, "ScreenLeft", cmpEqual, 166)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellAttachments.linkCopyCellAttachments object equals 597.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellAttachments.linkCopyCellAttachments, "ScreenTop", cmpEqual, 597)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellAttachments.linkCopyCellAttachments object equals 166.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode3.textnodeCopyCellAttachments.linkCopyCellAttachments, "ScreenLeft", cmpEqual, 166)
    #Clicks the 'linkView' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.linkView.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleHeader.linkToggleHeader object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleHeader.linkToggleHeader, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleHeader.linkToggleHeader object equals 218.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleHeader.linkToggleHeader, "ScreenLeft", cmpEqual, 218)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleToolbar.linkToggleToolbar object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleToolbar.linkToggleToolbar, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleToolbar.linkToggleToolbar object equals 218.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeToggleToolbar.linkToggleToolbar, "ScreenLeft", cmpEqual, 218)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.linkToggleLineNumbersshiftL object equals 200.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.linkToggleLineNumbersshiftL, "ScreenTop", cmpEqual, 200)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.linkToggleLineNumbersshiftL object equals 218.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.linkToggleLineNumbersshiftL, "ScreenLeft", cmpEqual, 218)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeView.linkCellToolbar object equals 224.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeView.linkCellToolbar, "ScreenTop", cmpEqual, 224)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeView.linkCellToolbar object equals 218.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode4.textnodeView.linkCellToolbar, "ScreenLeft", cmpEqual, 218)
    #Clicks the 'linkInsert' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode5.linkInsert.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellAboveA.linkInsertCellAbovea object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellAboveA.linkInsertCellAbovea, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellAboveA.linkInsertCellAbovea object equals 276.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellAboveA.linkInsertCellAbovea, "ScreenLeft", cmpEqual, 276)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellBelowB.linkInsertCellBelowb object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellBelowB.linkInsertCellBelowb, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellBelowB.linkInsertCellBelowb object equals 276.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode10.textnodeInsertCellBelowB.linkInsertCellBelowb, "ScreenLeft", cmpEqual, 276)
    #Clicks the 'linkCell' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode6.linkCell.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsCtrlEnter.linkRunCellsctrlEnter object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsCtrlEnter.linkRunCellsctrlEnter, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsCtrlEnter.linkRunCellsctrlEnter object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsCtrlEnter.linkRunCellsctrlEnter, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndSelectBelowSh.linkRunCellsAndSelectBelowshiftE object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndSelectBelowSh.linkRunCellsAndSelectBelowshiftE, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndSelectBelowSh.linkRunCellsAndSelectBelowshiftE object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndSelectBelowSh.linkRunCellsAndSelectBelowshiftE, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndInsertBelowAl.linkRunCellsAndInsertBelowaltEnt object equals 200.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndInsertBelowAl.linkRunCellsAndInsertBelowaltEnt, "ScreenTop", cmpEqual, 200)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndInsertBelowAl.linkRunCellsAndInsertBelowaltEnt object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunCellsAndInsertBelowAl.linkRunCellsAndInsertBelowaltEnt, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAll.linkRunAll object equals 224.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAll.linkRunAll, "ScreenTop", cmpEqual, 224)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAll.linkRunAll object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAll.linkRunAll, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllAbove.linkRunAllAbove object equals 248.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllAbove.linkRunAllAbove, "ScreenTop", cmpEqual, 248)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllAbove.linkRunAllAbove object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllAbove.linkRunAllAbove, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllBelow.linkRunAllBelow object equals 272.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllBelow.linkRunAllBelow, "ScreenTop", cmpEqual, 272)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllBelow.linkRunAllBelow object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeRunAllBelow.linkRunAllBelow, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCellType object equals 313.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCellType, "ScreenTop", cmpEqual, 313)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCellType object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCellType, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCurrentOutputs object equals 354.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCurrentOutputs, "ScreenTop", cmpEqual, 354)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCurrentOutputs object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkCurrentOutputs, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkAllOutput object equals 378.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkAllOutput, "ScreenTop", cmpEqual, 378)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkAllOutput object equals 339.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCell.linkAllOutput, "ScreenLeft", cmpEqual, 339)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCodeY.linkCodey object equals 313.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCodeY.linkCodey, "ScreenTop", cmpEqual, 313)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCodeY.linkCodey object equals 625.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCodeY.linkCodey, "ScreenLeft", cmpEqual, 625)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.linkMarkdownm object equals 337.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.linkMarkdownm, "ScreenTop", cmpEqual, 337)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnode12.linkRawNbconvertr object equals 625.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnode12.linkRawNbconvertr, "ScreenLeft", cmpEqual, 625)

def TC_67_70():
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode13.linkInterruptiI object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode13.linkInterruptiI, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode13.linkInterruptiI object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode13.linkInterruptiI, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode14.linkRestart00 object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode14.linkRestart00, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode14.linkRestart00 object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode14.linkRestart00, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode15.linkRestartClearOutput object equals 200.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode15.linkRestartClearOutput, "ScreenTop", cmpEqual, 200)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode15.linkRestartClearOutput object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode15.linkRestartClearOutput, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode16.linkRestartRunAll object equals 224.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode16.linkRestartRunAll, "ScreenTop", cmpEqual, 224)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode16.linkRestartRunAll object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode16.linkRestartRunAll, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode17.linkReconnect object equals 248.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode17.linkReconnect, "ScreenTop", cmpEqual, 248)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode17.linkReconnect object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode17.linkReconnect, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode18.linkShutdown object equals 272.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode18.linkShutdown, "ScreenTop", cmpEqual, 272)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode18.linkShutdown object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode18.linkShutdown, "ScreenLeft", cmpEqual, 391)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode19.linkChangeKernel object equals 313.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode19.linkChangeKernel, "ScreenTop", cmpEqual, 313)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode19.linkChangeKernel object equals 391.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode7.textnode19.linkChangeKernel, "ScreenLeft", cmpEqual, 391)
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8891/notebooks/Untitled.ipynb")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkWidgets' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.linkWidgets.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkSaveNotebookWidgetState object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkSaveNotebookWidgetState, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkSaveNotebookWidgetState object equals 459.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkSaveNotebookWidgetState, "ScreenLeft", cmpEqual, 459)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkClearNotebookWidgetState object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkClearNotebookWidgetState, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkClearNotebookWidgetState object equals 459.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkClearNotebookWidgetState, "ScreenLeft", cmpEqual, 459)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkDownloadWidgetState object equals 217.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkDownloadWidgetState, "ScreenTop", cmpEqual, 217)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkDownloadWidgetState object equals 459.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkDownloadWidgetState, "ScreenLeft", cmpEqual, 459)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkEmbedWidgets object equals 241.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkEmbedWidgets, "ScreenTop", cmpEqual, 241)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkEmbedWidgets object equals 459.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode8.textnode20.linkEmbedWidgets, "ScreenLeft", cmpEqual, 459)
    #Clicks the 'linkHelp' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.linkHelp.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode21.linkUserInterfaceTour object equals 152.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode21.linkUserInterfaceTour, "ScreenTop", cmpEqual, 152)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode21.linkUserInterfaceTour object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode21.linkUserInterfaceTour, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode22.linkKeyboardShortcutsh object equals 176.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode22.linkKeyboardShortcutsh, "ScreenTop", cmpEqual, 176)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode22.linkKeyboardShortcutsh object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode22.linkKeyboardShortcutsh, "ScreenLeft", cmpEqual, 536)
    #Drags the 'linkEditKeyboardShortcuts' object.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode23.linkEditKeyboardShortcuts.Drag(13, 13, 3, -9)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode23.linkEditKeyboardShortcuts object equals 200.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode23.linkEditKeyboardShortcuts, "ScreenTop", cmpEqual, 200)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode23.linkEditKeyboardShortcuts object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode23.linkEditKeyboardShortcuts, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNotebookHelp object equals 241.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNotebookHelp, "ScreenTop", cmpEqual, 241)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNotebookHelp object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNotebookHelp, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMarkdown object equals 265.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMarkdown, "ScreenTop", cmpEqual, 265)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMarkdown object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMarkdown, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPythonReference object equals 306.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPythonReference, "ScreenTop", cmpEqual, 306)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPythonReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPythonReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkIpythonReference object equals 330.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkIpythonReference, "ScreenTop", cmpEqual, 330)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNumpyReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkNumpyReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkScipyReference object equals 378.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkScipyReference, "ScreenTop", cmpEqual, 378)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkScipyReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkScipyReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMatplotlibReference object equals 402.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMatplotlibReference, "ScreenTop", cmpEqual, 402)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMatplotlibReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkMatplotlibReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkSympyReference object equals 426.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkSympyReference, "ScreenTop", cmpEqual, 426)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkSympyReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkSympyReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPandasReference object equals 450.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPandasReference, "ScreenTop", cmpEqual, 450)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPandasReference object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkPandasReference, "ScreenLeft", cmpEqual, 536)
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkAbout object equals 491.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkAbout, "ScreenTop", cmpEqual, 491)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkAbout object equals 536.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode9.textnode24.linkAbout, "ScreenLeft", cmpEqual, 536)
    #Clicks the 'panelNotebook' control.
    Aliases.browser.pageUntitledJupyterNotebook.panelNotebook.Click()
    #Clicks the 'panel2' control.
    Aliases.browser.pageUntitledJupyterNotebook.panel2.Click()
    #Clicks the 'panel3' control.
    Aliases.browser.pageUntitledJupyterNotebook.panel3.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.panel4 object equals 216.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panel4, "ScreenTop", cmpEqual, 216)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.panel4 object equals 120.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panel4, "ScreenLeft", cmpEqual, 120)
    #Clicks the 'panel5' control.
    Aliases.browser.pageUntitledJupyterNotebook.panel5.Click()
    #Checks whether the 'ScreenTop' property of the Aliases.browser.pageUntitledJupyterNotebook.panel6 object equals 258.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panel6, "ScreenTop", cmpEqual, 258)
    #Checks whether the 'ScreenLeft' property of the Aliases.browser.pageUntitledJupyterNotebook.panel6 object equals 120.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.panel6, "ScreenLeft", cmpEqual, 120)

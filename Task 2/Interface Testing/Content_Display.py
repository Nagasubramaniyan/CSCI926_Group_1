def TC_74():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8889/tree#running")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkFiles' link.
    Aliases.browser.pageHomePageSelectOrCreateANoteb.textnode.linkFiles.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.panel3 object equals 'Select items to perform actions on them.'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.panel3, "contentText", cmpEqual, "Select items to perform actions on them.")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonQuit object equals 'Quit'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonQuit, "contentText", cmpEqual, "Quit")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonLogout object equals 'Logout'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.buttonLogout, "contentText", cmpEqual, "Logout")

def TC_76():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8889/tree")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkRunning' link.
    Aliases.browser.pageHomePageSelectOrCreateANoteb.textnode.linkRunning.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.textnodeCurrentlyRunningJupyterP object equals 'Currently running Jupyter processes'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.textnodeCurrentlyRunningJupyterP, "contentText", cmpEqual, "Currently running Jupyter processes")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.linkTerminals object equals 'Terminals'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.linkTerminals, "contentText", cmpEqual, "Terminals")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.panel object equals 'There are no terminals running.'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.panel, "contentText", cmpEqual, "There are no terminals running.")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.linkNotebooks object equals 'Notebooks'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.linkNotebooks, "contentText", cmpEqual, "Notebooks")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.panel2 object equals 'There are no notebooks running.'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.panel2, "contentText", cmpEqual, "There are no notebooks running.")

def TC_77():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8889/tree#running")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkClusters' link.
    Aliases.browser.pageHomePageSelectOrCreateANoteb.textnode.linkClusters.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.textnode.linkClusters object equals 'Clusters'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.textnode.linkClusters, "contentText", cmpEqual, "Clusters")
    #Checks whether the 'contentText' property of the Aliases.browser.pageHomePageSelectOrCreateANoteb.panelClusters object equals 'Clusters tab is now provided by IPython parallel. See '
    #IPython parallel
    #' for installation details.'.
    aqObject.CheckProperty(Aliases.browser.pageHomePageSelectOrCreateANoteb.panelClusters, "contentText", cmpEqual, "Clusters tab is now provided by IPython parallel. See '\nIPython parallel\n' for installation details.")

def TC_78():
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.linkFile object equals 'File'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.linkFile, "contentText", cmpEqual, "File")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode3.linkEdit object equals 'Edit'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode3.linkEdit, "contentText", cmpEqual, "Edit")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode4.linkView object equals 'View'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode4.linkView, "contentText", cmpEqual, "View")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode5.linkInsert object equals 'Insert'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode5.linkInsert, "contentText", cmpEqual, "Insert")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode6.linkCell object equals 'Cell'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode6.linkCell, "contentText", cmpEqual, "Cell")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode7.linkKernel object equals 'Kernel'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode7.linkKernel, "contentText", cmpEqual, "Kernel")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode8.linkWidgets object equals 'Widgets'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode8.linkWidgets, "contentText", cmpEqual, "Widgets")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode9.linkHelp object equals 'Help'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode9.linkHelp, "contentText", cmpEqual, "Help")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnodePython3 object equals 'Python 3'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnodePython3, "contentText", cmpEqual, "Python 3")

def TC_79():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8889/notebooks/Downloads/Untitled.ipynb")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkFile' link.
    Aliases.browser.pageUntitled.textnode.textnode2.linkFile.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkNewNotebookdropdown object equals 'New Notebook
    #Dropdown'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkNewNotebookdropdown, "contentText", cmpEqual, "New Notebook\nDropdown")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeOpen.linkOpen object equals 'Open...'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeOpen.linkOpen, "contentText", cmpEqual, "Open...")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeMakeACopy.linkMakeACopy object equals 'Make a Copy...'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeMakeACopy.linkMakeACopy, "contentText", cmpEqual, "Make a Copy...")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeSaveAs.linkSaveAs object equals 'Save as...'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeSaveAs.linkSaveAs, "contentText", cmpEqual, "Save as...")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeRename.linkRename object equals 'Rename...'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeRename.linkRename, "contentText", cmpEqual, "Rename...")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.linkSaveAndCheckpointctrlS.textnodeSaveAndCheckpoint object equals 'Save and Checkpoint'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.linkSaveAndCheckpointctrlS.textnodeSaveAndCheckpoint, "contentText", cmpEqual, "Save and Checkpoint")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown object equals 'Revert to Checkpoint
    #Dropdown'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkRevertToCheckpointdropdown, "contentText", cmpEqual, "Revert to Checkpoint\nDropdown")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodePrintPreview.linkPrintPreview object equals 'Print Preview'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodePrintPreview.linkPrintPreview, "contentText", cmpEqual, "Print Preview")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkDownloadAsdropdown object equals 'Download as
    #Dropdown'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeFile.linkDownloadAsdropdown, "contentText", cmpEqual, "Download as\nDropdown")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt object equals 'Close and Halt'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt, "contentText", cmpEqual, "Close and Halt")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitled.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt object equals 'Close and Halt'.
    aqObject.CheckProperty(Aliases.browser.pageUntitled.textnode.textnode2.textnodeCloseAndHalt.linkCloseAndHalt, "contentText", cmpEqual, "Close and Halt")

def TC_80():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8888/notebooks/Downloads/Untitled.ipynb")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkFile' link.
    Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.linkFile.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode3.linkPython3 object equals 'Python 3'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode3.linkPython3, "contentText", cmpEqual, "Python 3")

def TC_81():
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode4.link20191210106 object equals '2019年12月10日星期二下午1点06分'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode4.link20191210106, "contentText", cmpEqual, "2019年12月10日星期二下午1点06分")

def TC_82():
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode5.linkAsciidocAsciidoc object equals 'AsciiDoc (.asciidoc)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode5.linkAsciidocAsciidoc, "contentText", cmpEqual, "AsciiDoc (.asciidoc)")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode6.linkHtmlHtml object equals 'HTML (.html)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode6.linkHtmlHtml, "contentText", cmpEqual, "HTML (.html)")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode7.linkLatexTex object equals 'LaTeX (.tex)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode7.linkLatexTex, "contentText", cmpEqual, "LaTeX (.tex)")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode8.linkMarkdownMd object equals 'Markdown (.md)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode8.linkMarkdownMd, "contentText", cmpEqual, "Markdown (.md)")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode9.linkNotebookIpynb object equals 'Notebook (.ipynb)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode9.linkNotebookIpynb, "contentText", cmpEqual, "Notebook (.ipynb)")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode10.linkPythonPy object equals 'Python (.py)'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode2.textnode10.linkPythonPy, "contentText", cmpEqual, "Python (.py)")

def TC_83():
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellsX.linkCutCellsx object equals 'Cut Cells
    #X'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellsX.linkCutCellsx, "contentText", cmpEqual, "Cut Cells\nX")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCopyCellsC.linkCopyCellsc object equals 'Copy Cells
    #C'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCopyCellsC.linkCopyCellsc, "contentText", cmpEqual, "Copy Cells\nC")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.linkDeleteCellsdD.textnodeDeleteCells object equals 'Delete Cells'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.linkDeleteCellsdD.textnodeDeleteCells, "contentText", cmpEqual, "Delete Cells")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellsX.linkCutCellsx.textnodeCutCells object equals 'Cut Cells'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellsX.linkCutCellsx.textnodeCutCells, "contentText", cmpEqual, "Cut Cells")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCopyCellsC.linkCopyCellsc.textnodeCopyCells object equals 'Copy Cells'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCopyCellsC.linkCopyCellsc.textnodeCopyCells, "contentText", cmpEqual, "Copy Cells")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.linkSplitCellctrlShiftMinus.textnodeSplitCell object equals 'Split Cell'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.linkSplitCellctrlShiftMinus.textnodeSplitCell, "contentText", cmpEqual, "Split Cell")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMergeCellAbove.linkMergeCellAbove object equals 'Merge Cell Above'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMergeCellAbove.linkMergeCellAbove, "contentText", cmpEqual, "Merge Cell Above")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMergeCellBelow.linkMergeCellBelow object equals 'Merge Cell Below'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMergeCellBelow.linkMergeCellBelow, "contentText", cmpEqual, "Merge Cell Below")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMoveCellUp.linkMoveCellUp object equals 'Move Cell Up'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMoveCellUp.linkMoveCellUp, "contentText", cmpEqual, "Move Cell Up")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMoveCellDown.linkMoveCellDown object equals 'Move Cell Down'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeMoveCellDown.linkMoveCellDown, "contentText", cmpEqual, "Move Cell Down")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeEditNotebookMetadata.linkEditNotebookMetadata object equals 'Edit Notebook Metadata'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeEditNotebookMetadata.linkEditNotebookMetadata, "contentText", cmpEqual, "Edit Notebook Metadata")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeFindAndReplace.linkFindAndReplace object equals 'Find and Replace'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeFindAndReplace.linkFindAndReplace, "contentText", cmpEqual, "Find and Replace")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellAttachments.linkCutCellAttachments object equals 'Cut Cell Attachments'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook.textnode.textnode11.textnodeCutCellAttachments.linkCutCellAttachments, "contentText", cmpEqual, "Cut Cell Attachments")

def TC_84_94():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("http://localhost:8891/notebooks/Untitled.ipynb")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkView' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.linkView.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeToggleHeader.linkToggleHeader object equals 'Toggle Header'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeToggleHeader.linkToggleHeader, "contentText", cmpEqual, "Toggle Header")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeToggleToolbar.linkToggleToolbar object equals 'Toggle Toolbar'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeToggleToolbar.linkToggleToolbar, "contentText", cmpEqual, "Toggle Toolbar")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.linkToggleLineNumbersshiftL.textnodeToggleLineNumbers object equals 'Toggle Line Numbers'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.linkToggleLineNumbersshiftL.textnodeToggleLineNumbers, "contentText", cmpEqual, "Toggle Line Numbers")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeView.linkCellToolbar object equals 'Cell Toolbar'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode2.textnodeView.linkCellToolbar, "contentText", cmpEqual, "Cell Toolbar")
    #Clicks the 'linkInsert' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode3.linkInsert.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode3.linkInsertCellAbovea.textnodeInsertCellAbove object equals 'Insert Cell Above'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode3.linkInsertCellAbovea.textnodeInsertCellAbove, "contentText", cmpEqual, "Insert Cell Above")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode3.linkInsertCellBelowb.textnodeInsertCellBelow object equals 'Insert Cell Below'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode3.linkInsertCellBelowb.textnodeInsertCellBelow, "contentText", cmpEqual, "Insert Cell Below")
    #Clicks the 'linkCell' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkCell.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsctrlEnter.textnodeRunCells object equals 'Run Cells'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsctrlEnter.textnodeRunCells, "contentText", cmpEqual, "Run Cells")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsAndSelectBelowshiftE.textnodeRunCellsAndSelectBelow object equals 'Run Cells and Select Below'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsAndSelectBelowshiftE.textnodeRunCellsAndSelectBelow, "contentText", cmpEqual, "Run Cells and Select Below")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsAndInsertBelowaltEnt.textnodeRunCellsAndInsertBelow object equals 'Run Cells and Insert Below'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.linkRunCellsAndInsertBelowaltEnt.textnodeRunCellsAndInsertBelow, "contentText", cmpEqual, "Run Cells and Insert Below")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeRunAllBelow.linkRunAllBelow object equals 'Run All Below'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeRunAllBelow.linkRunAllBelow, "contentText", cmpEqual, "Run All Below")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkCellType object equals 'Cell Type'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkCellType, "contentText", cmpEqual, "Cell Type")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkCurrentOutputs object equals 'Current Outputs'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkCurrentOutputs, "contentText", cmpEqual, "Current Outputs")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkAllOutput object equals 'All Output'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode4.textnodeCell.linkAllOutput, "contentText", cmpEqual, "All Output")
    #Clicks the 'linkKernel' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.linkKernel.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.linkInterruptiI.textnodeInterrupt object equals 'Interrupt'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.linkInterruptiI.textnodeInterrupt, "contentText", cmpEqual, "Interrupt")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.linkRestart00.textnodeRestart object equals 'Restart'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.linkRestart00.textnodeRestart, "contentText", cmpEqual, "Restart")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode6.linkRestartClearOutput object equals 'Restart & Clear Output'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode6.linkRestartClearOutput, "contentText", cmpEqual, "Restart & Clear Output")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode7.linkRestartRunAll object equals 'Restart & Run All'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode7.linkRestartRunAll, "contentText", cmpEqual, "Restart & Run All")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode8.linkReconnect object equals 'Reconnect'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode8.linkReconnect, "contentText", cmpEqual, "Reconnect")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode9.linkShutdown object equals 'Shutdown'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode9.linkShutdown, "contentText", cmpEqual, "Shutdown")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode10.linkChangeKernel object equals 'Change kernel'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode10.linkChangeKernel, "contentText", cmpEqual, "Change kernel")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode10.linkChangeKernel object equals 'Change kernel'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode5.textnode10.linkChangeKernel, "contentText", cmpEqual, "Change kernel")
    #Clicks the 'linkWidgets' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.linkWidgets.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkSaveNotebookWidgetState object equals 'Save Notebook Widget State'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkSaveNotebookWidgetState, "contentText", cmpEqual, "Save Notebook Widget State")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkClearNotebookWidgetState object equals 'Clear Notebook Widget State'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkClearNotebookWidgetState, "contentText", cmpEqual, "Clear Notebook Widget State")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkDownloadWidgetState object equals 'Download Widget State'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkDownloadWidgetState, "contentText", cmpEqual, "Download Widget State")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkEmbedWidgets object equals 'Embed Widgets'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode11.textnode12.linkEmbedWidgets, "contentText", cmpEqual, "Embed Widgets")
    #Clicks the 'linkHelp' link.
    Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.linkHelp.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode14.linkUserInterfaceTour object equals 'User Interface Tour'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode14.linkUserInterfaceTour, "contentText", cmpEqual, "User Interface Tour")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode15.linkKeyboardShortcutsh object equals 'Keyboard Shortcuts
    #H'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode15.linkKeyboardShortcutsh, "contentText", cmpEqual, "Keyboard Shortcuts\nH")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode16.linkEditKeyboardShortcuts object equals 'Edit Keyboard Shortcuts'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnode16.linkEditKeyboardShortcuts, "contentText", cmpEqual, "Edit Keyboard Shortcuts")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkNotebookHelp object equals 'Notebook Help'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkNotebookHelp, "contentText", cmpEqual, "Notebook Help")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkMarkdown object equals 'Markdown'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkMarkdown, "contentText", cmpEqual, "Markdown")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodePythonReference object equals 'Python Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodePythonReference, "contentText", cmpEqual, "Python Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeIpythonReference object equals 'IPython Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeIpythonReference, "contentText", cmpEqual, "IPython Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeNumpyReference object equals 'NumPy Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeNumpyReference, "contentText", cmpEqual, "NumPy Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeScipyReference object equals 'SciPy Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeScipyReference, "contentText", cmpEqual, "SciPy Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeMatplotlibReference object equals 'Matplotlib Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeMatplotlibReference, "contentText", cmpEqual, "Matplotlib Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeSympyReference object equals 'SymPy Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodeSympyReference, "contentText", cmpEqual, "SymPy Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodePandasReference object equals 'pandas Reference'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.textnodePandasReference, "contentText", cmpEqual, "pandas Reference")
    #Checks whether the 'contentText' property of the Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkAbout object equals 'About'.
    aqObject.CheckProperty(Aliases.browser.pageUntitledJupyterNotebook2.textnode.textnode13.textnodeUserInterfaceTourKeyboar.linkAbout, "contentText", cmpEqual, "About")

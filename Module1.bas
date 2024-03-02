Attribute VB_Name = "Module1"
Sub Macro1()

Dim r As Range

Set r = Selection

For Each cell In r
    cell = cell + 4
Next cell

End Sub

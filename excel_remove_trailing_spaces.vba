Sub RemoveTrailingSpaces()
    Dim rng As Range
    Dim cell As Range

    On Error Resume Next
    ' Zaznacz zakres z danymi
    Set rng = Application.InputBox("Zaznacz zakres komórek:", Type:=8)

    For Each cell In rng
        If Not IsEmpty(cell.Value) Then
            cell.Value = RTrim(cell.Value)
        End If
    Next cell
End Sub
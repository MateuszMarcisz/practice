Sub RemoveLeadingAndTrailingSpaces()
    Dim rng As Range
    Dim cell As Range

    On Error Resume Next
    ' Zaznacz zakres z danymi
    Set rng = Application.InputBox("Zaznacz zakres komórek:", Type:=8)
    On Error GoTo 0

    If rng Is Nothing Then Exit Sub ' Wyjście, jeśli użytkownik anulował wybór

    For Each cell In rng
        If Not IsEmpty(cell.Value) Then
            cell.Value = Trim(cell.Value)
        End If
    Next cell

    MsgBox "Usunięto spacje początkowe i końcowe z wybranego zakresu.", vbInformation
End Sub
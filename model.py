def id3(row):
    if row.Subs_groups=='high':
        row.Play='Yes'
    else:
        if row.Views_groups=='high':
            row.Play = 'Yes'
        else:
            row.Play='No'
    return row
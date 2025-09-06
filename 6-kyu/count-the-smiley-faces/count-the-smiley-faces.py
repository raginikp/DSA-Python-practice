def count_smileys(arr):
    valid_smileys = {":)", ":D", ";)", ";D", ":-)", ":-D", ";-)", ";-D", ":~)", ":~D", ";~)", ";~D"}
    return sum(1 for face in arr if face in valid_smileys)
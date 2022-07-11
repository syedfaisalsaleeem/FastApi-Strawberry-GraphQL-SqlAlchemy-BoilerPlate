get_users_query = """
query MyQuery {
  users {
    id
    name
    stickynotes {
      createdDatetime
      id
      text
      userId
    }
  }
}
"""

get_specific_user_query = """
query MyQuery2 {
  user(userId: 1) {
    id
    name
    stickynotes {
      id
      text
      createdDatetime
      userId
    }
  }
}
"""

get_sticky_notes_query = """
query MyQuery3 {
  stickynotes {
    createdDatetime
    id
    text
    userId
  }
}
"""

get_specific_sticky_note_query = """
query MyQuery4 {
  stickynote(stickynoteId: 1) {
    createdDatetime
    id
    text
    userId
  }
}"""
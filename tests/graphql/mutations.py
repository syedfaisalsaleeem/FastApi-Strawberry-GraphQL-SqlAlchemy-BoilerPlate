create_user = """
    mutation MyMutation {
        addUser(name: "test") {
            ... on AddUser {
            id
            name
            }
            ... on UserExists {
            message
            }
        }
    }
"""

create_sticky_notes = """
mutation MyMutation {
  addStickynotes(text: "demo text", userId: 1) {
    ... on StickyNotes {
      id
      createdDatetime
      text
      userId
    }
    ... on UserNotFound {
      message
    }
    ... on UserNameMissing {
      message
    }
  }
}
"""

delete_specific_user = """
mutation MyMutation {
  deleteUser(userId: 1) {
    ... on UserDeleted {
      message
    }
    ... on UserNotFound {
      message
    }
    ... on UserIdMissing {
      message
    }
  }
}
"""

update_specific_sticky_note = """
mutation MyMutation3 {
  updateStickynote(stickynoteId: 1, text: "new text") {
    ... on StickyNotes {
      id
      createdDatetime
      text
      userId
    }
    ... on StickyNotesNotFound {
      message
    }
  }
}"""

delete_specific_sticky_note = """
mutation MyMutation4 {
  deleteStickynote(stickynoteId: 1) {
    ... on StickyNotesDeleted {
      message
    }
    ... on StickyNotesNotFound {
      message
    }
  }
}
"""
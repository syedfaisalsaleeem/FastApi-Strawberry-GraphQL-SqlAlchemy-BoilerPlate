create_user = """
    mutation MyMutation {
        add_user(name: "test") {
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
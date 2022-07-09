import strawberry

from src.graphql.scalars.stickynotes_scalar import StickyNotes, StickyNotesDeleted, StickyNotesNotFound
from src.graphql.scalars.user_scalar import UserNameMissing, UserNotFound


AddStickyNotesResponse = strawberry.union("AddStickyNotesResponse", (StickyNotes, UserNotFound, UserNameMissing))
UpdateStickyNotesResponse = strawberry.union("UpdateStickyNotesResponse", (StickyNotes, StickyNotesNotFound))
DeleteStickyNotesResponse = strawberry.union("DeleteStickyNotesResponse", (StickyNotesDeleted, StickyNotesNotFound))
#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from .block_user import BlockUser
from .delete_profile_photos import DeleteProfilePhotos
from .get_common_chats import GetCommonChats
from .get_me import GetMe
from .get_profile_photos import GetProfilePhotos
from .get_profile_photos_count import GetProfilePhotosCount
from .get_users import GetUsers
from .iter_profile_photos import IterProfilePhotos
from .set_profile_photo import SetProfilePhoto
from .unblock_user import UnblockUser
from .update_profile import UpdateProfile
from .update_username import UpdateUsername
from .delete_account import DeleteAccount


class Users(
    BlockUser,
    GetCommonChats,
    GetProfilePhotos,
    SetProfilePhoto,
    DeleteProfilePhotos,
    GetUsers,
    GetMe,
    UpdateUsername,
    GetProfilePhotosCount,
    IterProfilePhotos,
    UnblockUser,
    UpdateProfile,
    DeleteAccount,
):
    pass

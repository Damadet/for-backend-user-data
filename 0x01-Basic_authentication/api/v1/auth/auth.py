#!/usr/bin/env python3
from flask import request



class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handles require authentication
        
        
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """handles authentication header
        
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None
    
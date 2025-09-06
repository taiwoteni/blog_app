# Django Blog Comment Functionality Fix - Todo List

## Issues Identified:
1. **URL Pattern Conflicts**: Duplicate comment URL patterns in blog/urls.py and comments/urls.py
2. **Template URL Reference Mismatch**: Template uses 'add_comment' but URL pattern uses 'add-comment'
3. **Dual View Implementations**: Both function-based and class-based views for comments
4. **URL Configuration Issues**: Both URL patterns are included in main urls.py

## Tasks to Complete:

### 1. Fix URL Pattern Conflicts
- [ ] Remove duplicate comment URL from blog/urls.py
- [ ] Standardize on function-based view from comments app
- [ ] Fix URL name consistency

### 2. Fix Template URL References
- [ ] Update post_detail.html template to use correct URL name
- [ ] Ensure form action points to correct URL pattern

### 3. Verify View Implementation
- [ ] Confirm comments/views.py function-based view works correctly
- [ ] Remove unused CommentCreateView from blog/views.py
- [ ] Test comment submission functionality

### 4. Update URL Configuration
- [ ] Ensure proper URL inclusion order in django_blog/urls.py
- [ ] Test all comment-related URLs work correctly

### 5. Final Testing
- [ ] Test comment creation on a post
- [ ] Verify comment display on post detail page
- [ ] Check authentication requirements work properly

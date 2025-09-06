# Django Blog Application

A full-featured blog application built with Django, featuring user authentication, post management, categories, tags, comments, and search functionality.

## Features

- **User Authentication**: Registration, login, logout, password reset
- **Blog Management**: Create, read, update, delete posts
- **Categories & Tags**: Organize posts with categories and tags
- **Comments**: Users can comment on posts
- **Search**: Search posts by title and content
- **User Profiles**: User-specific post listings
- **Responsive Design**: Bootstrap-based responsive templates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/taiwoteni/blog_app.git
cd blog_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Blog Endpoints

| Method | URL | Description | Authentication |
|--------|-----|-------------|----------------|
| GET | `/` | Home page - list all posts | None |
| GET | `/post/<slug>/` | Post detail view | None |
| GET | `/post/new/` | Create new post form | Required |
| POST | `/post/new/` | Submit new post | Required |
| GET | `/post/<slug>/update/` | Edit post form | Required (Author only) |
| POST | `/post/<slug>/update/` | Update post | Required (Author only) |
| GET | `/post/<slug>/delete/` | Delete post confirmation | Required (Author only) |
| POST | `/post/<slug>/delete/` | Delete post | Required (Author only) |
| GET | `/user/<username>/` | User's posts listing | None |
| GET | `/category/<slug>/` | Posts by category | None |
| GET | `/tags/<tag_slug>/` | Posts by tag | None |
| GET | `/search/` | Search posts | None |

### Authentication Endpoints

| Method | URL | Description | Authentication |
|--------|-----|-------------|----------------|
| GET | `/accounts/register/` | User registration form | None |
| POST | `/accounts/register/` | Create new account | None |
| GET | `/accounts/login/` | Login form | None |
| POST | `/accounts/login/` | User login | None |
| POST | `/accounts/logout/` | User logout | Required |
| GET | `/accounts/profile/` | User profile | Required |
| GET | `/accounts/password_change/` | Password change form | Required |
| POST | `/accounts/password_change/` | Change password | Required |
| GET | `/accounts/password_reset/` | Password reset form | None |
| POST | `/accounts/password_reset/` | Request password reset | None |
| GET | `/accounts/reset/<uidb64>/<token>/` | Password reset confirmation | None |
| POST | `/accounts/reset/<uidb64>/<token>/` | Set new password | None |

### Comment Endpoints

| Method | URL | Description | Authentication |
|--------|-----|-------------|----------------|
| POST | `/post/<slug>/comment/` | Add comment to post | Required |

## Models

### Post Model
- `title`: Post title (CharField)
- `slug`: Unique slug for URL (SlugField)
- `content`: Post content (TextField)
- `date_posted`: Publication date (DateTimeField)
- `author`: Foreign key to User
- `category`: Foreign key to Category (optional)
- `tags`: TaggableManager for tags

### Category Model
- `name`: Category name (CharField)
- `slug`: Unique slug for URL (SlugField)

### Comment Model
- `post`: Foreign key to Post
- `author`: Foreign key to User
- `content`: Comment content (TextField)
- `created_at`: Comment creation date (DateTimeField)

## URL Patterns

### Main URL Configuration (django_blog/urls.py)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('comments.urls')),
]
```

### Blog URLs (blog/urls.py)
```python
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<slug:slug>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='category_posts'),
    path('tags/<slug:tag_slug>/', TagPostListView.as_view(), name='post_by_tag'),
    path('search/', SearchPostListView.as_view(), name='search'),
]
```

### Authentication URLs (accounts/urls.py)
```python
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
```

### Comment URLs (comments/urls.py)
```python
urlpatterns = [
    path('post/<slug:slug>/comment/', views.add_comment, name='add-comment'),
]
```

## Views

### Blog Views (blog/views.py)
- `PostListView`: List all blog posts
- `PostDetailView`: Display single post with comments
- `PostCreateView`: Create new post (login required)
- `PostUpdateView`: Edit existing post (author only)
- `PostDeleteView`: Delete post (author only)
- `UserPostListView`: List posts by specific user
- `CategoryPostListView`: List posts by category
- `TagPostListView`: List posts by tag
- `SearchPostListView`: Search posts by keyword
- `CommentCreateView`: Add comment to post (login required)

### Authentication Views (accounts/views.py)
- `register`: User registration
- `profile`: User profile page

### Comment Views (comments/views.py)
- `add_comment`: Add comment to post (login required)

## Templates

The application uses Django templates with Bootstrap styling:

- `base.html`: Base template with navigation
- `home.html`: Homepage with post listings
- `post_detail.html`: Individual post view with comments
- `post_create.html`: Post creation form
- `post_update.html`: Post edit form
- `post_delete.html`: Post deletion confirmation
- `category_posts.html`: Category-based post listing
- `comment_form.html`: Comment submission form

Authentication templates are located in `accounts/templates/accounts/`.

## Static Files

Static files (CSS, JavaScript, images) are served from the `static/` directory:
- `static/css/auth.css`: Authentication-specific styles
- `static/images/`: Image assets
- `static/js/`: JavaScript files

## Dependencies

Key dependencies listed in `requirements.txt`:
- Django
- django-taggit (for tag functionality)
- Other Django-related packages

## Deployment

The project includes a `Procfile` for deployment on Heroku or similar platforms.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

from pydantic import BaseModel


class Owner:
    big_photo: str | None
    full_name_display: str
    gravatar_id: str
    id: int
    is_active: bool
    photo: str | None
    username: str


class GetListProjects:
    anon_permissions: list
    blocked_code: str | None
    created_date: str
    creation_template: int
    default_epic_status: int
    default_issue_status: int
    default_issue_type: int
    default_points: int
    default_priority: int
    default_severity: int
    default_task_status: int
    default_us_status: int
    description: str
    i_am_admin: bool
    i_am_member: bool
    i_am_owner: bool
    id: int
    is_backlog_activated: bool
    is_contact_activated: bool
    is_epics_activated: bool
    is_fan: bool
    is_featured: bool
    is_issues_activated: bool
    is_kanban_activated: bool
    is_looking_for_people: bool
    is_private: bool
    is_watcher: bool
    is_wiki_activated: bool
    logo_big_url: str | None
    logo_small_url: str | None
    looking_for_people_note: str
    members: list
    modified_date: str
    my_homepage: bool
    my_permissions: list
    name: str
    notify_level: int
    owner: Owner
    public_permissions: list
    slug: str
    tags: list
    tags_colors: dict
    total_activity: int
    total_activity_last_month: int
    total_activity_last_week: int
    total_activity_last_year: int
    total_closed_milestones: int
    total_fans: int
    total_fans_last_month: int
    total_fans_last_week: int
    total_fans_last_year: int
    total_milestones: int | None
    total_story_points: int | None
    total_watchers: int
    totals_updated_datetime: str
    videoconferences: None
    videoconferences_extra_data: str | None

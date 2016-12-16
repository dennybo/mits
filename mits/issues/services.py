from tags.models import Tag
from models import *


def pack_issue_tags(issue):
    result = []

    all_tags = issue.project.tag_set.all()
    issue_tags = issue.tags.all()

    for tag in issue_tags:
        result.append((True, tag))

    for tag in all_tags:
        if tag not in issue_tags:
            result.append((False, tag))

    return result

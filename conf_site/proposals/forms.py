from django import forms

from markitup.widgets import MarkItUpWidget

from .models import Proposal


class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TutorialForm(ProposalForm):
    """
    Custom form for Carolinas tutorials with custom help text.

    See http://stackoverflow.com/a/3287893/113527.

    """
    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        # Add additional "additional_notes" help text.
        self.fields["additional_notes"].help_text += (
            "<br><strong>Please let us know if you would prefer a "
            "90 minute or 120 minute tutorial.</strong>"
        )

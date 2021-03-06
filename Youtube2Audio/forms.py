from django import forms


class YoutubeForm(forms.Form):
    youtube_url = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control mr-sm-2",
                                                              "id": "urlInput",
                                                              "placeholder": "https://www.youtube.com/example123"}),
                                 label="Youtube URL:")

    def get_url(self):
        if self.is_valid():
            return self.cleaned_data["youtube_url"]

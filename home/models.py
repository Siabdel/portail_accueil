from re import I
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import BaseChooserPanel, RichTextField, RichTextFieldPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from .blocks import CardBlock


from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django.utils import timezone

class HomePage(Page):
    """ Page home Model """
    template_name = "/templates/home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(blank=True)
    banner_body = RichTextField(null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey("wagtailcore.Page",
                                blank=True, null=True,
                                on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel('banner_body', classname="full"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]


    class Meta:
        verbose_name = "Home page site demo"
        verbose_name_plural = "Accueil Bakery"



#---------------------------------
#-- Bootstrap template page 
#---------------------------------

class BootstrapTemplatePage(Page):
    
    #intro = models.CharField(max_length=250, )
    created = models.DateField("date de creation", auto_now_add=True)

    body = StreamField([
        ('card_block', CardBlock()),
    ], blank=True)


    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    
    
    class Meta:
        verbose_name = "Bootstrap template page"
        verbose_name_plural = "bootstrap templates "
#--------------------------------
#---- Standard page
#--------------------------------
class StandardPage(Page):
    created = models.DateField("date de creation")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('card_block', CardBlock()),

    ], blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('created'),
        StreamFieldPanel('body'),
    ]
    

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core import blocks as wagtail_blocks
from wagtail.images.blocks import ImageChooserBlock

from streams.blocks import TitleBlock
from streams import blocks
from home.models import new_table_options

class FlexPage(Page):
    parent_page_types=["home.HomePage", "flex.FlexPage"]
    body=StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html")),
        ("pricing_table", blocks.PricingTableBlock(
            table_options=new_table_options,
        )),
        
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
        )),
        ("large_image", ImageChooserBlock(
            help_text="This image will be cropped to 1200px by 775px",
            template="streams/large_image_block.html",
        ))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"
        
from django.test import TestCase
from .forms import SlotForm

# Create your tests here.


class TestSlotForm(TestCase):

    def test_slot_name_is_required(self):
        form = SlotForm({'firstname': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('firstname', form.errors.keys())
        self.assertEqual(form.errors['firstname'][0], 'This field is required.')
        form = SlotForm({'lastname': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('lastname', form.errors.keys())
        self.assertEqual(form.errors['lastname'][0], 'This field is required.')
        form = SlotForm({'slot_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slot_date', form.errors.keys())
        self.assertEqual(form.errors['slot_date'][0], 'This field is required.')
        form = SlotForm({'slot_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slot_time', form.errors.keys())
        self.assertEqual(form.errors['slot_time'][0], 'This field is required.')


    def test_submit_field_is_not_required(self):
        form = SlotForm({'firstname': 'Test Todo Items'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = SlotForm()
        self.assertEqual(form.Meta.fields, ['firstname', 'lastname', 'slot_date', 'slot_time', 'submit'])



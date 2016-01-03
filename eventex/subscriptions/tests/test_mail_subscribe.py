from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Diego Sorrilha', cpf='12345678901',
                    email='diego@x4start.com', phone='21-99999-1187')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'diego@x4start.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Diego Sorrilha',
            '12345678901',
            'diego@x4start.com',
            '21-99999-1187'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

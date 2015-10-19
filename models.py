# -*- coding: utf-8 -*-

from openerp import models, fields, api


# class mediatek(models.Model):
#     _name = 'mediatek.mediatek'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


# TODO: Add res.partner
# TODO: Add relations


class Document(models.Model):
    _name = 'mediatek.document'

    name = fields.Char('Title',
                       required=True,
                       select=True)
    type = fields.Selection([
        ('cd', 'C.D.'),
        ('book', 'Book')
    ])
    image = fields.Binary('Image')
    desc = fields.Text('Description')
    purchase_date = fields.Date('Purchase date')
    status = fields.Selection([
        ('ok', 'OK'),
        ('burn', 'Burned'),
        ('lost', 'Lost')
    ])


class Loan(models.Model):
    _name = 'mediatek.loan'

    date = fields.Date('Date',
                       default=fields.Date.today())
    status = fields.Selection('Status')


class Artist(models.Model):
    _name = 'mediatek.artist'

    name = fields.Char('Name')
    homepage = fields.Char('Homepage')

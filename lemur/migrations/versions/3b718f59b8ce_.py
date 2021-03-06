"""Refactors Accounts to Destinations

Revision ID: 3b718f59b8ce
Revises: None
Create Date: 2015-07-09 17:44:55.626221

"""

# revision identifiers, used by Alembic.
revision = '3b718f59b8ce'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificate_account_associations')
    op.drop_table('accounts')
    op.add_column('destinations', sa.Column('plugin_name', sa.String(length=32), nullable=True))
    op.drop_index('ix_elbs_account_id', table_name='elbs')
    op.drop_constraint(u'elbs_account_id_fkey', 'elbs', type_='foreignkey')
    op.drop_column('elbs', 'account_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('elbs', sa.Column('account_id', sa.BIGINT(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'elbs_account_id_fkey', 'elbs', 'accounts', ['account_id'], ['id'])
    op.create_index('ix_elbs_account_id', 'elbs', ['account_id'], unique=False)
    op.drop_column('destinations', 'plugin_name')
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), server_default=sa.text(u"nextval('accounts_id_seq'::regclass)"), nullable=False),
    sa.Column('account_number', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('label', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'accounts_pkey'),
    sa.UniqueConstraint('account_number', name=u'accounts_account_number_key'),
        postgresql_ignore_search_path=False
    )
    op.create_table('certificate_account_associations',
    sa.Column('account_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('certificate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['account_id'], [u'accounts.id'], name=u'certificate_account_associations_account_id_fkey', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['certificate_id'], [u'certificates.id'], name=u'certificate_account_associations_certificate_id_fkey', ondelete=u'CASCADE')
    )
    ### end Alembic commands ###

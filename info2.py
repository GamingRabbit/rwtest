import discord
from discord.ext import commands

class Members():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joined(self,member: discord.Member):
        await self.client.say('{0.name} joined in {0.joined_at}'.format(member))

        
    @commands.command(pass_context=True)
    async def info(self,ctx,member: discord.Member=None):
        'Show info about a member'
        if member is None:
            member = ctx.message.author
        em = discord.Embed()
        em.add_field(name='Name', value='{0.name}'.format(member))
        em.add_field(name='ID', value='{0.id}'.format(member))
        em.add_field(name='Top Role', value='{0.top_role}'.format(member))
        em.add_field(name='Roles', value=', '.join(g.name for g in member.roles))
        em.add_field(name='Joined', value='{0.joined_at}'.format(member))
        em.set_thumbnail(url=member.avatar_url)
        await self.client.say(embed=em)
        
    @commands.command(pass_context=True)
    async def changelog(self):
      em = discord.Embed()
      em.add_field(name='0.8. and previous versions', value='I don"t remeber everything what I"ve done in every version')
      em.add_field(name='0.9.',  value='added a new Cog called Info2')
      await self.client.say(embed=em)

def setup(client):
    client.add_cog(Members(client))

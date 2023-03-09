import click


@click.command('transform_image')
@click.argument('filepath')
# @click.option('--op', default="compress")
def transform_image(filepath):
    print(f'transform_image function\nfilepath arg: {filepath}')

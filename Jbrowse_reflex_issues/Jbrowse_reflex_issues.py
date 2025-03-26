import reflex as rx
from typing import Any


### these are wrap code ;document link: https://reflex.dev/docs/wrapping-react/guide/#full-guide
class JBrowseLinearGenomeView(rx.NoSSRComponent):
    library: str = "@jbrowse/react-linear-genome-view2"
    tag: str = "JBrowseLinearGenomeView"

    view_state: rx.Var[Any]


def j_browse_linear_genome_view(view_state: dict | rx.Var[dict]):
    return JBrowseLinearGenomeView.create(
        ### use this code to run createViewState maybe in nodejs.
        view_state=rx.Var(
            "createViewState",
            _var_data=rx.vars.VarData(
                imports={"@jbrowse/react-linear-genome-view2": "createViewState"}
            ),
        )
        .to(rx.vars.FunctionVar)
        .call(view_state)
    )


###############################################################

view_stat = {
    "assembly": {
        "name": "hg38",
        "sequence": {
            "type": "ReferenceSequenceTrack",
            "trackId": "GRCh38-ReferenceSequenceTrack",
            "adapter": {
                "type": "BgzipFastaAdapter",
                "uri": "https://jbrowse.org/genomes/GRCh38/fasta/hg38.prefix.fa.gz",
            },
        },
        "refNameAliases": {
            "adapter": {
                "type": "RefNameAliasAdapter",
                "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/hg38_aliases.txt",
            }
        },
    },
    "tracks": [
        {
            "type": "FeatureTrack",
            "trackId": "genes",
            "name": "NCBI RefSeq Genes",
            "assemblyNames": ["hg38"],
            "category": ["Genes"],
            "adapter": {
                "type": "Gff3TabixAdapter",
                "gffGzLocation": {
                    "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz"
                },
                "index": {
                    "location": {
                        "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.tbi"
                    }
                },
            },
            "textSearching": {
                "textSearchAdapter": {
                    "type": "TrixTextSearchAdapter",
                    "textSearchAdapterId": "gff3tabix_genes-index",
                    "uri": "https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.ix",
                    "assemblyNames": ["GRCh38"],
                }
            },
        }
    ],
}


class BrowseState(rx.State):
    pass


@rx.page(route="/")
def test_jbrowse() -> rx.Component:
    return rx.flex(
        rx.heading("Test JBrowse"),
        j_browse_linear_genome_view(view_stat),
        direction="column",
        width="100%",
        justify="center",
        padding="4rem",
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
    )
)

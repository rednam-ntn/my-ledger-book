from typing import Any, Dict, List, Optional, Set, Tuple  # noqa: F401

import fitz
from typing_extensions import TypedDict


class SlimShape(TypedDict):
    """Shape info object

    Args:
        idx (int): shape index in `input_shapes`
        rect (fitz.Rect): shape rect bbox
        fill (Tuple[float, float, float]): shape fill color PDF RGB
        props (Dict[str, Any]): other shape properties
        items (List[list]): shape items, each item is a small shape with list of points,
    """

    idx: int
    rect: fitz.Rect
    fill: Tuple[float, float, float]
    props: Dict[str, Any]
    items: List[list]


SIZE_INFO = Tuple[Tuple[float, str], Tuple[float, str]]


class FactoryTickets(TypedDict):
    """Factory tickets info object

    Args:
        id (int): Ticket ID
        cad_url (str): CAD's URL
        pieces_urls (List[str]): pieces' URL
    """

    id: str
    cad_url: str
    pieces_urls: List[str]
